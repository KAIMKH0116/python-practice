# 「合計を計算する」という関数
def goukei_keisan(data):
    goukei = 0
    for i in range(len(data)):
        goukei = goukei + data[i]
    return goukei

# 使用例
uriage = [150000, 180000, 120000, 200000, 160000]
kekka = goukei_keisan(uriage)
print(kekka)