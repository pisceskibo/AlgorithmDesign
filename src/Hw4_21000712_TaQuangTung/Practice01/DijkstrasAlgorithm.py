# Dijkstra’s Algorithm
import time
import matplotlib.pyplot as plt
import sys


def dijkstra(graph, start = 0):
    # Số lượng đỉnh trong đồ thị
    numVertices = len(graph)
    
    # Tạo mảng distances để lưu khoảng cách ngắn nhất từ start đến mỗi đỉnh
    distances = [sys.maxsize] * numVertices
    distances[start] = 0
    
    # Mảng boolean để kiểm tra xem đỉnh nào đã được xử lý
    visited = [False] * numVertices
    
    for _ in range(numVertices):
        # Tìm đỉnh có khoảng cách tối thiểu từ tập hợp các đỉnh chưa được xử lý
        min_distance = sys.maxsize
        for v in range(numVertices):
            if distances[v] < min_distance and not visited[v]:
                min_distance = distances[v]
                u = v
                
        # Đánh dấu đỉnh đã được xử lý
        visited[u] = True
        
        # Cập nhật khoảng cách đến các đỉnh lân cận của đỉnh được chọn
        for v in range(numVertices):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
    
    print("Đỉnh \t Khoảng Cách từ Đỉnh Bắt Đầu")
    for i in range(numVertices):
        print(f"{i} \t\t {distances[i]}")

def getTime(distanceMatrix):
    listTime = []
    for element in distanceMatrix:
        time1 = time.perf_counter_ns()
        dijkstra(element)
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

