
products = {
    'りんご': 50,
    'みかん': 0,
    'ぶどう': 30,
    'メロン': 0,
    'いちご': 15
}

# ① productsをfor文でループしてください
for product_name in products:
    # ② 在庫が0の場合「◯◯は在庫切れです」と出力してください
    if products[product_name] == 0:
        print(product_name + 'は在庫切れです')
    # ③ 在庫が0以外の場合「◯◯の在庫は△△個です」と出力してください
    else:
        print(product_name + 'の在庫は' + str(products[product_name]) +'個です')

# ④ 在庫ありの商品を在庫数が多い順にランキング表示してください
# 在庫ありの商品だけ取り出す
in_stock = {}
for product_name in products:
    if products[product_name] != 0:
        in_stock[product_name] = products[product_name]

print('--- 在庫ランキング ---')
ranked = sorted(in_stock, key=lambda x: in_stock[x], reverse=True)
for i, name in enumerate(ranked, 1):
    print(str(i) + '位 ' + name + '：' + str(in_stock[name]) + '個')

