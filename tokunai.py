import pandas as pd

# Excelを読み込む
df = pd.read_excel('滞納者リスト.xlsx')

# 滞納月数で分類
def 督促ランク(月数):
    if 月数 >= 3:
        return '督促状'
    elif 月数 >= 1:
        return 'リマインド'
    else:
        return 'なし'

# ランク列を追加
df['対応'] = df['滞納月数'].apply(督促ランク)

# 結果を表示
print(df)

# Excelで出力
df.to_excel('督促リスト.xlsx', index=False)
print('督促リスト.xlsx を作成しました')
