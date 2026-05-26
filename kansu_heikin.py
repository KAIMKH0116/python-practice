def heikin_keisan(data):
    goukei = 0
    for i in range(len(data)):
        goukei = goukei + data[i]
    heikin = goukei / len(data)
    return heikin

def saikouten_sagasu(data):
    saikouten = data[0]
    for i in range(len(data)):
        if data[i] > saikouten:
            saikouten = data[i]
    return saikouten

# 使用例
uriage = [150000, 180000, 120000, 200000, 160000]
kekka = heikin_keisan(uriage)
print(kekka)