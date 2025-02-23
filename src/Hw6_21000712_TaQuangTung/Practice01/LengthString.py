# Cho xâu X có độ dài m, xâu Y có độ dài n. Tìm xâu con chung của X và Y có độ dài lớn nhất.
import random
import time
import matplotlib.pyplot as plt

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def randomString(pairXY):
    # Giá trị ASCII của 'a' là 97 và 'z' là 122
    a = 97
    z = 122
    finalPair = []
    for i in range(len(pairXY)):
        temp = []
        tempX = []
        tempY = []
        # Random cho X
        for j1 in range(pairXY[i][0]):
            # Tạo số ngẫu nhiên từ a đến z
            random_number = random.randint(a, z)

            # Chuyển đổi số ngẫu nhiên thành ký tự tương ứng
            random_character = chr(random_number)
            tempX.append(random_character)
        temp.append(tempX)
        
        # Random cho Y
        for j1 in range(pairXY[i][1]):
            # Tạo số ngẫu nhiên từ a đến z
            random_number = random.randint(a, z)

            # Chuyển đổi số ngẫu nhiên thành ký tự tương ứng
            random_character = chr(random_number)
            tempY.append(random_character)
        temp.append(tempY)

        finalPair.append(temp)
    return finalPair

def getTime(X, Y):
    listTime = []
    for i in range(len(X)):
        time1 = time.perf_counter_ns()
        longest_common_subsequence(X[i], Y[i])
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ biểu đồ
def drawTime(nameXY, timeList):
    plt.plot(nameXY, timeList)
    plt.title("Biểu đồ thời gian bài toán xâu con chung")
    plt.xlabel("Name Array")
    plt.ylabel("Time (ns)")
    plt.show()

if __name__ == "__main__":
    pairXY = [[10, 9], [100, 90], [1000, 900]]
    X = [randomString(pairXY)[i][0] for i in range(len(randomString(pairXY)))]
    Y = [randomString(pairXY)[i][1] for i in range(len(randomString(pairXY)))]
    listTime = getTime(X, Y)

    nameXY = []
    for i in range(len(pairXY)):
        labelString = f"[{pairXY[i][0]}, {pairXY[i][1]}]"
        nameXY.append(labelString)
    print(nameXY)

    drawTime(nameXY, listTime)

""" Cơ sở QHĐ:
F[i][0] = F[0][j] = 0
X[i] = Y[j] => F[i][j] = F[i - 1][j - 1] + 1
X[i] != Y[j] => F[i][j] = max(F[i][j - 1], F[i - 1][j])
"""