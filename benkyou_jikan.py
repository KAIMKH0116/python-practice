benkyou_jikan = [30,45,20,50,35,40,25]
print(benkyou_jikan[0])
goukei = 0
for i in range(7):
    goukei = goukei + benkyou_jikan[i]
print(goukei)
heikin = goukei /  7
print(heikin)