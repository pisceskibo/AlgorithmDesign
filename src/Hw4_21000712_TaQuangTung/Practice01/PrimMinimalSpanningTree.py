# Thuật toán Prim tìm cây bao trùm nhỏ nhất
import time
import matplotlib.pyplot as plt


def prim(distanceMatrix):
    numVertices = len(distanceMatrix)
    selected = [False] * numVertices    # Đánh dấu đỉnh đã được chọn
    selected[0] = True                  # Bắt đầu từ đỉnh đầu tiên
    numEdges = 0                        # Số cạnh đã được thêm vào

    print("Các cạnh trong cây bao trùm nhỏ nhất:")
    
    # Lặp cho đến khi đã thêm tất cả các đỉnh vào cây (MST)
    while (numEdges < numVertices - 1):
        minimum = float('inf')
        a = b = 0
        for m in range(numVertices):
            if selected[m]:
                for n in range(numVertices):
                    if ((not selected[n]) and distanceMatrix[m][n]):  
                        # Nếu một đỉnh chưa được chọn và có cạnh nối từ m đến n
                        if minimum > distanceMatrix[m][n]:
                            minimum = distanceMatrix[m][n]
                            a = m
                            b = n
        print(f"{chr(65 + a)} - {chr(65 + b)}: {distanceMatrix[a][b]}")
        selected[b] = True
        numEdges += 1

# Hàm lấy thời gian
def getTime(distanceMatrix):
    listTime = []
    for element in distanceMatrix:
        time1 = time.perf_counter_ns()
        prim(element)
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ dữ liệu thời gian
def drawTime(sizeList, timeList):
    plt.plot(sizeList, timeList)
    plt.title("Biểu đồ thời gian thuật toán Prim")
    plt.xlabel("Size")
    plt.ylabel("Time (ns)")

    plt.show()

if __name__ == "__main__":
    # Ma trận khoảng cách giữa các đỉnh
    distanceMatrix1 = [
        [0, 7, 0, 5],      # A
        [7, 0, 8, 9],      # B
        [0, 8, 0, 0],      # C
        [5, 9, 0, 0]       # D
    ]

    distanceMatrix2 = [
        [0, 7, 0, 5, 0],      # A
        [7, 0, 8, 9, 7],      # B
        [0, 8, 0, 0, 5],      # C
        [5, 9, 0, 0, 15],     # D
        [0, 7, 5, 15, 0]      # E
    ]
    distanceMatrix3 = [
        [0, 7, 0, 5, 0, 0, 0],      # A
        [7, 0, 8, 9, 7, 0, 0],      # B
        [0, 8, 0, 0, 5, 0, 0],      # C
        [5, 9, 0, 0, 15, 6, 0],     # D
        [0, 7, 5, 15, 0, 8, 9],     # E
        [0, 0, 0, 6, 8, 0, 11],     # F
        [0, 0, 0, 0, 9, 11, 0]      # G
    ]

    distanceMatrix = [distanceMatrix1, distanceMatrix2, distanceMatrix3]
    sizeMatrix = [len(distanceMatrix1), len(distanceMatrix2), len(distanceMatrix3)]
    timeList = getTime(distanceMatrix)
    drawTime(sizeMatrix, timeList)
