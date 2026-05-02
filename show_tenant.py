def show_tenant(tenant):
    print("部屋番号：" + tenant['room'] + " 名前：" + tenant['name'] + " 滞納額：" + str(tenant['debt']) + "円")

show_tenant({'room': '101', 'name': '田中太郎', 'debt': 50000})
show_tenant({'room': '202', 'name': '佐藤花子', 'debt': 0})
