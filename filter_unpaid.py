def filter_unpaid(tenants):
    result = []
    for tenant in tenants:
        if tenant['debt'] > 0:
            result.append(tenant)
    return result

tenants = [
    {'room': '101', 'name': '田中太郎', 'debt': 50000},
    {'room': '102', 'name': '佐藤花子', 'debt': 0},
    {'room': '103', 'name': '鈴木一郎', 'debt': 150000},
    {'room': '104', 'name': '高橋誠',   'debt': 0},
    {'room': '105', 'name': '伊藤美咲', 'debt': 100000}
]
result = filter_unpaid(tenants)
for tenant in result:
    print(tenant['name'])
