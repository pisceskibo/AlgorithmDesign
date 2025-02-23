# Bài toán đổi tiền
from random import randrange
import time
import matplotlib.pyplot as plt

# Phương pháp đổi tiền
def changeMoney(coins, coinTarget, sum = 0):
    i = 0               # Index
    count = 0           # Biến đếm
    newCoins = []       # Mảng gồm số tiền

    while i < (len(coins)):
        sum += coins[i]
        if (sum <= coinTarget):
            count += 1
        else:
            sum -= coins[i]
            newCoins.append(count)
            count = 0
            i += 1
    return newCoins

# Hiển thị tiền
def printChangeMoney(coinTarget):
    timeList = []
    for coin_target in coinTarget:
        # print(f"Đổi {coin_target}$ sang các tờ tiền lẻ sau:")
        time1 = time.perf_counter_ns()
        newCoins = changeMoney(coins, coin_target)
        time2 = time.perf_counter_ns()
        # for i in range(len(coins)):
        #     print(f"\tCó {newCoins[i]} tờ {coins[i]}$")
        # print()
        timeList.append(time2 - time1)
    return timeList

# Vẽ dữ liệu thời gian
def drawTime(coins, timeList):
    plt.plot(coins, timeList)
    plt.title("Biểu đồ thời gian toán đổi tiền")
    plt.xlabel("Coin Targets")
    plt.ylabel("Time (ns)")

    plt.show()


if __name__ == "__main__":
    coins = [50, 20, 10, 5, 2, 1]
    coins.sort(reverse=True)
    coinTarget = [randrange(50, 100) for i in range(len(coins))]
    timeList = printChangeMoney(coinTarget)
    drawTime(coinTarget, timeList)
    