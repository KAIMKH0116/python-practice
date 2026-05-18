import streamlit as st
import json
import re

st.set_page_config(
    page_title="SUNO.AI 音楽評価ツール",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎵 SUNO.AI 音楽評価ツール - Phase 1")
st.markdown("日本語言語学的な観点から、SUNO.AIで生成した音楽を評価します（Claude.ai ハイブリッド版）")

# セッション状態の初期化
if "evaluation_prompt" not in st.session_state:
    st.session_state.evaluation_prompt = None

if "form_data" not in st.session_state:
    st.session_state.form_data = {
        "prompt": "",
        "lyrics": "",
        "genre": "",
        "target": ""
    }

# ========== フロー判定 ==========
if st.session_state.evaluation_prompt is None:
    # ========== 入力フォームフェーズ ==========
    st.markdown("### 📋 ワークフロー")
    st.markdown("""
    1. **ここで** 音楽情報を入力
    2. **「🎯 評価プロンプトを生成」** をクリック
    3. **プロンプトをコピー**
    4. **Claude.ai を別タブで開く** → https://claude.ai
    5. **プロンプトを貼り付けて実行**
    6. **結果をここに貼り付け**
    """)
    
    st.markdown("---")
    st.markdown("### 📝 評価対象の音楽情報を入力してください")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("制作情報")
        prompt = st.text_area(
            "SUNO.AIに入力したプロンプト *",
            value=st.session_state.form_data["prompt"],
            height=100,
            placeholder="例: upbeat pop song about summer, Japanese lyrics, 2 minutes...",
            key="prompt_input"
        )
        st.session_state.form_data["prompt"] = prompt
        
        genre = st.text_input(
            "ジャンル（オプション）",
            value=st.session_state.form_data["genre"],
            placeholder="例: J-pop, indie, dance...",
            key="genre_input"
        )
        st.session_state.form_data["genre"] = genre
    
    with col_right:
        st.subheader("配信情報")
        target = st.text_input(
            "配信目標（オプション）",
            value=st.session_state.form_data["target"],
            placeholder="例: YouTube, Spotify, TikTok...",
            key="target_input"
        )
        st.session_state.form_data["target"] = target
    
    # 歌詞入力
    st.markdown("---")
    st.subheader("🎤 歌詞情報")
    lyrics = st.text_area(
        "実際の歌詞（SUNO.AI出力） *",
        value=st.session_state.form_data["lyrics"],
        height=150,
        placeholder="ここに SUNO.AI が生成した歌詞をコピペしてください",
        key="lyrics_input"
    )
    st.session_state.form_data["lyrics"] = lyrics
    
    # プロンプト生成ボタン
    st.markdown("---")
    col_btn_left, col_btn_right = st.columns([1, 4])
    
    with col_btn_left:
        is_ready = bool(prompt.strip() and lyrics.strip())
        generate_button = st.button(
            "🎯 評価プロンプトを生成",
            disabled=not is_ready,
            use_container_width=True,
            type="primary"
        )
    
    with col_btn_right:
        if not is_ready:
            st.caption("⚠️ プロンプトと歌詞を入力してください")
    
    # ========== プロンプト生成実行 ==========
    if generate_button and is_ready:
        evaluation_prompt = f"""あなたは日本語言語学の専門家です。SUNO.AIで生成された音楽の「日本語言語学的品質」を評価してください。

【作成時のプロンプト】
{prompt}

【ジャンル】
{genre if genre else "未指定"}

【配信目標】
{target if target else "未指定"}

【実際の歌詞】
{lyrics}

【評価項目】（合計50点）
1. 音読み・訓読みの正誤性（20点）
   - 漢字がAIによって正しい読み方で発音されているか
   - 音読み・訓読みの違いや誤りはないか
   
2. 歌詞と発音の一致度（15点）
   - 表記された歌詞と実際の発音が一致しているか
   - 言葉が正確に発音されているか
   
3. 日本語の自然さ・流暢さ（15点）
   - 日本語として自然か
   - 不自然な点や違和感はないか

【評価形式】
以下のJSON形式で回答してください。JSONのみを返してください。他の説明は不要です：
{{
  "score_accuracy": XX,
  "score_pronunciation": XX,
  "score_natural": XX,
  "total": XX,
  "issues": ["問題点1", "問題点2"],
  "improvements": ["改善案1", "改善案2"],
  "suno_prompt": "SUNO.AIへの再プロンプト案"
}}"""
        
        st.session_state.evaluation_prompt = evaluation_prompt
        st.rerun()

# ========== プロンプト表示フェーズ ==========
else:
    st.markdown("### 📋 Claude.ai に貼り付けるプロンプト")
    
    st.code(st.session_state.evaluation_prompt, language="text")
    
    st.markdown("---")
    
    # ボタン群
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    
    with col_btn1:
        if st.button("📋 コピー", use_container_width=True):
            st.info("✅ クリップボードにコピーされました！手動で Ctrl + V で貼り付けてください。")
    
    with col_btn2:
        st.markdown(
            """
            <a href="https://claude.ai" target="_blank" style="text-decoration: none;">
                <button style="width: 100%; padding: 10px; background-color: #4a90e2; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
                    🌐 Claude.ai を開く
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    st.markdown("### 📝 Claude.ai での実行手順")
    st.markdown("""
    1. **上のプロンプトをコピー** （📋 ボタンをクリック）
    2. **「🌐 Claude.ai を開く」をクリック** （別タブで開く）
    3. **新規チャットを開く**（またはチャット入力欄をクリック）
    4. **プロンプトを貼り付け** （Ctrl + V）
    5. **Enter キーで実行**
    6. **Claude.ai の回答をすべて選択して、コピー**
    """)
    
    st.markdown("---")
    
    st.markdown("### 💡 Claude.ai の回答を貼り付け")
    
    result_input = st.text_area(
        "Claude.ai からの回答（JSON）をここに貼り付けてください",
        height=250,
        placeholder="[Claude.ai の回答全体をここに貼り付け]\n例:\n{\n  \"score_accuracy\": 18,\n  \"score_pronunciation\": 14,\n  ...\n}"
    )
    
    col_process1, col_process2, col_process3 = st.columns(3)
    
    with col_process1:
        if st.button("✅ 結果を処理", use_container_width=True, type="primary"):
            if result_input.strip():
                try:
                    # JSON を抽出
                    json_match = re.search(r'\{[\s\S]*\}', result_input)
                    
                    if json_match:
                        result = json.loads(json_match.group())
                        
                        # 結果を表示
                        st.markdown("---")
                        st.markdown("### 📊 評価結果")
                        
                        # 総合スコア
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.metric(
                                label="日本語言語学的スコア",
                                value=f"{result.get('total', 0)} / 50"
                            )
                        
                        with col2:
                            total = result.get('total', 0)
                            if total >= 40:
                                status = "✅ OK"
                            elif total >= 30:
                                status = "⚠️ 要注意"
                            else:
                                status = "❌ 要改善"
                            st.metric(label="判定", value=status)
                        
                        # 詳細スコア
                        st.markdown("#### 詳細スコア")
                        score_cols = st.columns(3)
                        with score_cols[0]:
                            st.metric("音読み・訓読み", f"{result.get('score_accuracy', 0)} / 20")
                        with score_cols[1]:
                            st.metric("歌詞と発音", f"{result.get('score_pronunciation', 0)} / 15")
                        with score_cols[2]:
                            st.metric("自然さ・流暢性", f"{result.get('score_natural', 0)} / 15")
                        
                        # 問題点
                        if result.get("issues"):
                            st.markdown("#### ⚠️ 問題点")
                            for issue in result["issues"]:
                                st.warning(f"• {issue}")
                        
                        # 改善案
                        if result.get("improvements"):
                            st.markdown("#### 💡 改善案")
                            for imp in result["improvements"]:
                                st.info(f"• {imp}")
                        
                        # SUNO.AI用プロンプト案
                        if result.get('suno_prompt'):
                            st.markdown("#### 🎯 SUNO.AI 再作成用プロンプト案")
                            st.code(result.get('suno_prompt', ''), language="text")
                        
                        st.success("✅ 評価結果を処理しました！")
                    else:
                        st.error("❌ JSON が見つかりませんでした。Claude.ai の回答をすべてコピーして、もう一度貼り付けてください。")
                
                except json.JSONDecodeError as e:
                    st.error(f"❌ JSON の解析に失敗しました。エラー: {str(e)}")
            else:
                st.warning("⚠️ 回答を貼り付けてください")
    
    with col_process2:
        st.write("")
    
    with col_process3:
        if st.button("🔄 新規評価へ", use_container_width=True):
            st.session_state.evaluation_prompt = None
            st.session_state.form_data = {"prompt": "", "lyrics": "", "genre": "", "target": ""}
            st.rerun()

# ========== サイドバー情報 ==========
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ ハイブリッド版について")
st.sidebar.markdown("""
**このバージョンの特徴：**
- ✅ クレジット不要
- ✅ Claude.ai の無料枠が使える
- ✅ 高精度評価
- ✅ プライベートで安全

**ワークフロー：**
1. プロンプト・歌詞を入力
2. 評価プロンプトを自動生成
3. Claude.ai に貼り付けて実行
4. 結果をここに貼り付け
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 使い方")
st.sidebar.markdown("""
1. **情報入力**：プロンプト、歌詞、ジャンル、配信目標
2. **プロンプト生成**：「評価プロンプトを生成」をクリック
3. **Claude.ai で実行**：プロンプトをコピして貼り付け
4. **結果処理**：Claude.ai の回答をここに貼り付け
5. **評価確認**：スコアと改善案を確認
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 次フェーズ（Phase 2）")
st.sidebar.markdown("""
- プロデューサー視点
- トレンド分析視点
- 一般リスナー視点
- 複数視点の統合評価
""")