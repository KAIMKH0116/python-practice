def count_by_status(tenants):
    result = {'unpaid': 0, 'paid': 0} 
    for tenant in tenants:
        if tenant['debt'] == 0:
            result['paid'] += 1   
        else:
            result['unpaid'] += 1
    return result

tenants = [
    {'name': '田中太郎', 'debt': 50000},
    {'name': '佐藤花子', 'debt': 0},
    {'name': '鈴木一郎', 'debt': 150000},
    {'name': '高橋誠',   'debt': 0},
    {'name': '伊藤美咲', 'debt': 100000}
]
result = count_by_status(tenants)
print(result)
