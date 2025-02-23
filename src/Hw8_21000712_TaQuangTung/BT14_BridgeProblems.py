"""
Nước A có M thành phố, nước B có N thành phố
Mỗi thành phố của A liên kết cây cầu với thành phố của B (cây cầu không cắt nhau)
=> Tìm ra cách bắc cầu nhiều nhất 
"""

from random import randint

def max_bridges(M, N, countryAB):
    # Khởi tạo mảng ban đầu
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    # Quy hoạch động
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if countryAB[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Truy vết tìm nghiệm
    m, n = M, N
    bridges_coordinates = []
    while m > 0 and n > 0:
        if countryAB[m - 1][n - 1] == 1:
            bridges_coordinates.append((m, n))
            m -= 1
            n -= 1
        else:
            if dp[m - 1][n] >= dp[m][n - 1]:
                m -= 1
            else:
                n -= 1
    
    return dp[M][N], bridges_coordinates

if __name__ == "__main__":
    M = int(input("Số lượng thành phố A: "))
    N = int(input("Số lượng thành phố B: "))
    countryAB = [[randint(0, 1) for _ in range(N)] for _ in range(M)]
    print(countryAB)

    max_bridges, bridges = max_bridges(M, N, countryAB)
    print("Số cây cầu tối đa là:", max_bridges)
    print("Tọa độ tương ứng cho cây cầu bắc qua là:", bridges)
