# Thuật toán Kruskal tìm cây bao trùm nhỏ nhất
import time
import matplotlib.pyplot as plt

# Tìm đỉnh cha của đỉnh i trong mảng parent 
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Hợp nhất hai tập hợp con chứa x và y 
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(distanceMatrix):
    numVertices = len(distanceMatrix)
    graph = []
    for i in range(numVertices):
        for j in range(i+1, numVertices):  # Chỉ xét một nửa của ma trận vì đồ thị không hướng
            if distanceMatrix[i][j] != 0:
                graph.append([i, j, distanceMatrix[i][j]])

    # Sắp xếp các cạnh theo trọng số tăng dần
    graph.sort(key=lambda item: item[2])

    parent = [i for i in range(numVertices)]
    rank = [0 for _ in range(numVertices)]

    MST = []
    for edge in graph:
        u, v, weight = edge
        u_root = find(parent, u)
        v_root = find(parent, v)
        if u_root != v_root:
            MST.append(edge)
            union(parent, rank, u_root, v_root)

    print("Các cạnh trong cây bao trùm nhỏ nhất:")
    for u, v, weight in MST:
        print(f"{chr(65 + u)} -- {chr(65 + v)}: {weight}")

# Hàm lấy thời gian
def getTime(distanceMatrix):
    listTime = []
    for element in distanceMatrix:
        time1 = time.perf_counter_ns()
        kruskal(element)
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ dữ liệu thời gian
def drawTime(sizeList, timeList):
    plt.plot(sizeList, timeList)
    plt.title("Biểu đồ thời gian thuật toán Kruskal")
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
