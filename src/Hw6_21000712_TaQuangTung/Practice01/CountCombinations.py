# Bài toán đếm tổ hợp:
"""
C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
C(n, 0) = C(n, n) = 1
C(n, k) = 0 với n < k
"""

import matplotlib.pyplot as plt
import time

def combination(n, k):
    # Bước 1: Tạo một bảng DP với (k+1) hàng và (n+1) cột (thêm)
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    
    # Bước 2: Khởi tạo các trường hợp cơ bản
    for i in range(k+1):
        dp[i][i] = 1  # Các phần tử trên đường chéo chính bằng 1 => C(i, i) = 1

    for i in range(n + 1):
        dp[0][i] = 1 # Các phần tử iC0 = 1 với i thuộc [0, n]
    
    # Bước 3: Áp dụng công thức truy hồi
    for i in range(1, k + 1):
        for j in range(i + 1, n - k + i + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j - 1]
    
    return dp[k][n]

# Hàm lấy thời gian chạy
def getTime(sizeN, sizeK):
    timeList = []
    for i in range(len(sizeN)):
        time1 = time.perf_counter_ns()
        combination(sizeN[i], sizeK[i])
        time2 = time.perf_counter_ns()
        timeList.append(time2 - time1)
        print(f"C({sizeN[i]}, {sizeK[i]}) = {combination(sizeN[i], sizeK[i])}") 
    return timeList

# Vẽ biểu đồ
def drawTime(nameArray, timeList):
    plt.plot(nameArray, timeList)
    plt.title("Biểu đồ thời gian bài toán tổ hợp")
    plt.xlabel("Name Array")
    plt.ylabel("Time (ns)")
    plt.show()

if __name__ == "__main__":
    sizeN = [10, 100, 1000]
    sizeK = [5, 50, 500]
    nameC = [f"C({sizeN[i]}, {sizeK[i]})" for i in range(len(sizeN))]
    timeList = getTime(sizeN, sizeK)
    # drawTime(nameC, timeList)
