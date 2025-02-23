# Bài toán cái túi (0 - 1 Knapsack)
from random import randrange
import time
import matplotlib.pyplot as plt

def knapsack(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

def randomValue(size):
    valueArray = []
    for length in size:
        temp = []
        for i in range(length):
            temp.append(randrange(1, 100))
        temp.sort()
        valueArray.append(temp)
    return valueArray

def randomWeight(size):
    weightArray = []
    for length in size:
        temp = []
        for i in range(length):
            temp.append(randrange(1, 10))
        temp.sort()
        weightArray.append(temp)
    return weightArray

def getTime(size, valueArray, weightArray):
    listTime = []
    for i in range(len(size)):
        time1 = time.perf_counter_ns()
        knapsack(valueArray[i], weightArray[i], size[i])
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ biểu đồ
def drawTime(size, timeList):
    plt.plot(size, timeList)
    plt.title("Biểu đồ thời gian bài toán túi xách")
    plt.xlabel("Name Array")
    plt.ylabel("Time (ns)")
    plt.show()

if __name__ == "__main__":
    size = [10, 100, 1000]
    valueArray = randomValue(size)
    weightArray = randomWeight(size)
    timeList = getTime(size, valueArray, weightArray)

    drawTime(size, timeList)