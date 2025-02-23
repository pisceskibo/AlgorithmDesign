# Bài toán đổi tiền

coins = [50, 10, 5, 1]
coins.sort(reverse=True)
coinTarget = 78

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


if __name__ == "__main__":
    print(f"Đổi {coinTarget}$ sang các tờ tiền lẻ sau:")
    newCoins = changeMoney(coins, coinTarget)
    for i in range(len(coins)):
        print(f"\tCó {newCoins[i]} tờ {coins[i]}$")