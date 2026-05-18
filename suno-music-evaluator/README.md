# 🎵 SUNO.AI 音楽評価ツール - Phase 1

SUNO.AIで生成した音楽を、複数の視点から自動評価するツール。  
Phase 1 では「日本語言語学者視点」での評価を実装しています。

---

## 📋 必要な準備

### 1. Anthropic API キー取得

1. https://console.anthropic.com/ にアクセス
2. アカウント作成またはログイン
3. **API Keys** セクションから新しいキーを生成
4. キーをコピー（例: `sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx`）

### 2. ローカル環境設定

```bash
# プロジェクトフォルダに移動
cd C:\Users\OWNER\Desktop\suno-evaluator

# Python仮想環境作成（推奨）
python -m venv venv

# 仮想環境を有効化
venv\Scripts\activate

# パッケージをインストール
pip install -r requirements.txt
```

### 3. .env ファイル作成

`.env.example` をコピー → `.env` に リネーム

`.env` ファイルを開いて編集：

APIキーの部分を実際のキーに置き換え

---

## 🚀 実行方法

```bash
streamlit run app.py
```

ブラウザが自動で開き、`http://localhost:8501` で起動します。

---

## 📚 使い方

1. **プロンプト入力**：SUNO.AIに入力した内容をコピペ
2. **歌詞入力**：SUNO.AI出力の歌詞をコピペ
3. **評価実行**：「評価を開始」をクリック
4. **結果確認**：スコアと改善案を確認
5. **再作成**：改善プロンプト案でSUNO再作成

---

## 🎯 Phase 1 機能

✅ 日本語言語学者視点での評価  
✅ 音読み・訓読みの正誤検証  
✅ 歌詞と発音の一致度チェック  
✅ 自然さ・流暢性の評価  
✅ SUNO.AI再プロンプト案の自動生成  

---

**作成日**: 2026年5月13日  
**バージョン**: Phase 1.0