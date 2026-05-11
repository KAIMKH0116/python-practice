
items = {'coffee': 300, 'juice': 200, 'water': 100}

for item_name in items:
    print(item_name + 'は' + str(items[item_name]) + '円です')
    
    # 支払い金額を入力させて変数 payment に代入してください
    payment = input('支払い金額を入力してください:')
    # payment を数値に変換して変数 price に代入してください
    price = int(payment)
    # おつりを計算して変数 change に代入してください
    change = price - items[item_name]
    # 「おつりは◯◯円です」と出力してください
    print('おつりは' + str(change) + '円です')

