# Bài toán xếp balo (0-1)
import time
from random import randint
import matplotlib.pyplot as plt

# Mảng lấy giá trị tỷ số
def sortByRatio(arrayMoney, arrayItems):
    ratioArray = [arrayMoney[i]/arrayItems[i] for i in range(len(arrayItems))]

    items = zip(arrayMoney, arrayItems, ratioArray)
    sortedItem = sorted(items, reverse=True, key=lambda x : x[2])

    newMoney = [sortedItem[i][0] for i in range(len(sortedItem))]
    newWeight = [sortedItem[i][1] for i in range(len(sortedItem))]

    return newMoney, newWeight

def knapSack(newWeight, newMoney, maxWeight, total = 0):
    i = 0
    count = 0
    while i < len(arrayItems):
        total += newMoney[i]
        maxWeight -= newWeight[i]

        if maxWeight >= 0:
            count += 1
        else:
            maxWeight += newWeight[i]
            total -= newMoney[i]
            count = 0
            i += 1
    return total        

# Vẽ dữ liệu thời gian
def drawTime(maxWeight, timeList):
    plt.plot(maxWeight, timeList)
    plt.title("Biểu đồ thời gian toán xếp ba lô")
    plt.xlabel("Max Weight")
    plt.ylabel("Time (ns)")

    plt.show()

if __name__ == "__main__":
    arrayItems = [5, 3, 2, 4, 10]
    arrayMoney = [10, 5, 3, 6, 5]
    
    newMoney, newWeight = sortByRatio(arrayMoney, arrayItems)   
    # maxWeight = 27
    maxWeight = [20, 27, 30, 40, 50]
    timeList = []
    for i in range(len(maxWeight)):
        time1 = time.perf_counter_ns()
        knapSack(newWeight, newMoney, maxWeight[i])
        time2 = time.perf_counter_ns()
        timeList.append(time2 - time1)
    drawTime(maxWeight, timeList)
