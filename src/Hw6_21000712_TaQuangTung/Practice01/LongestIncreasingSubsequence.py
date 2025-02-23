# Dãy con tăng dần dài nhất
import time
from random import randrange
import matplotlib.pyplot as plt

def longestSubsequence(array):
    n = len(array)

    # Khởi tạo mảng dp, mọi phần tử đều bắt đầu bằng 1 (mảng theo thứ tự)
    dp = [1] * n

    # Tính dp[i] cho mọi i từ 1 đến n-1
    for i in range(1, n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Tìm giá trị lớn nhất trong mảng dp
    return max(dp)

# Sinh ngẫu nhiên các phần tử trong mảng
def randomValue(sizeArray):
    randArray = []
    for size in sizeArray:
        randTemp = []
        for i in range(size):
            randTemp.append(randrange(100))
        randArray.append(randTemp)
    return randArray

# Hàm lấy các giá trị ứng với mảng
def getTime(randArray):
    timeList = []
    for i in range(len(randArray)):
        time1 = time.perf_counter_ns()
        longestSubsequence(randArray[i])
        time2 = time.perf_counter_ns()
        timeList.append(time2 - time1)
    return timeList

# Vẽ biểu đồ
def drawTime(nameArray, timeList):
    plt.plot(nameArray, timeList)
    plt.title("Biểu đồ thời gian bài toán mảng con tăng dần nhỏ nhất")
    plt.xlabel("Size of Array")
    plt.ylabel("Time (ns)")
    plt.show()

if __name__ == "__main__":
    sizeArray = [10, 50, 100, 500, 1000]
    randArray = randomValue(sizeArray)
    timeList = getTime(randArray)
    drawTime(sizeArray, timeList)
