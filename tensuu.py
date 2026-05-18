tensuu = [85, 92, 78, 88]
print(tensuu[0])
saikouten = tensuu[0]
for i in range(4):
    if tensuu[i] > saikouten:
        saikouten = tensuu[i]
print(saikouten)