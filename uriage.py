uriage = [150000, 180000, 120000, 200000, 160000]
print(uriage[0])
goukei = 0
for i in range(5):
    goukei = goukei + uriage[i]
print(goukei)
heikin = goukei / 5
print(heikin)
saikouten = uriage[0]
for i in range(5):
    if uriage[i] > saikouten:
        saikouten = uriage[i]
print(saikouten)