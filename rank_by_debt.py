def rank_by_debt(tenants):
    ranked = sorted(tenants, key=lambda x: x['debt'], reverse=True)
    for i, tenant in enumerate(ranked, 1):
        print(f"{i}位 {tenant['name']}：{tenant['debt']:,}円")

tenants = [
    {'name': '田中太郎', 'debt': 50000},
    {'name': '佐藤花子', 'debt': 0},
    {'name': '鈴木一郎', 'debt': 150000},
    {'name': '高橋誠',   'debt': 0},
    {'name': '伊藤美咲', 'debt': 100000}
]

rank_by_debt(tenants)
