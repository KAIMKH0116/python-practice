def find_max_debt(tenants):
    max = 0
    max_tenant = None
    for tenant in tenants:
        if tenant['debt'] > max:
            max = tenant['debt']
            max_tenant = tenant
    return max_tenant['name']

tenants = [
    {'room': '101', 'name': '田中太郎', 'debt': 50000},
    {'room': '102', 'name': '佐藤花子', 'debt': 0},
    {'room': '103', 'name': '鈴木一郎', 'debt': 150000},
    {'room': '104', 'name': '高橋誠',   'debt': 0},
    {'room': '105', 'name': '伊藤美咲', 'debt': 100000}
]
print(find_max_debt(tenants))