def calc_summary(numbers):
    total = sum(numbers)
    average = round(total/len(numbers))
    print("合計:" + str(total) + " 平均: " + str(average))

calc_summary([50000, 150000, 0, 250000, 100000])
