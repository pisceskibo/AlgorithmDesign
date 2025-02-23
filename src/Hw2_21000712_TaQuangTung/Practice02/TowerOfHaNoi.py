import time
import matplotlib.pyplot as plt

# Đệ quy tháp
def towerRecursive(number, start, end, mid):
    if number == 1:
        print(f"Move 1 from {start} to {end}")
        return
    else:
        towerRecursive(number - 1, start, mid, end)
        print(f"Move {number} from {start} to {end}")
        towerRecursive(number - 1, mid, end, start)

def towerEliminateRecursive(n, start, end, mid):
    start, end, mid = 'A', 'C', 'B'
    # Số bước tối thiểu để giải quyết bài toán Tháp Hà Nội là 2^n - 1
    total_moves = 2**n - 1
    
    # Ba cột trong bài toán được đánh số là A, B, C
    # Cột A là cột bắt đầu, B là cột trung gian, và C là cột đích
    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            print(f"Move disk from {start if n % 2 == 0 else end} to {end if n % 2 == 0 else start}")
        elif move % 3 == 2:
            print(f"Move disk from {start} to {mid}")
        else:
            print(f"Move disk from {mid if n % 2 == 0 else end} to {end if n % 2 == 0 else mid}")


# Vẽ đồ thị thời gian so sánh
def data():
    nameTime = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]
    listTimeRecursive = []
    listTimeEliminate = []
    for i in range(len(nameTime)):
        start1 = time.perf_counter_ns()
        towerRecursive(nameTime[i], 'A', 'C', 'B')
        end1 = time.perf_counter_ns()
        spaceRecursive = end1 - start1
        listTimeRecursive.append(spaceRecursive)

        start2 = time.perf_counter_ns()
        towerEliminateRecursive(nameTime[i], 'A', 'C', 'B')
        end2 = time.perf_counter_ns()
        spaceEliminate = end2 - start2
        listTimeEliminate.append(spaceEliminate)

    return nameTime, listTimeRecursive, listTimeEliminate


if __name__ == "__main__":
    nameTime, listTimeRecursive, listTimeEliminate = data()
    plt.plot(nameTime, listTimeRecursive, color='red', label='Recursive')
    plt.plot(nameTime, listTimeEliminate, color='green', label='Eliminate')
    plt.title('Biểu đồ thời gian chạy của thuật toán TowerOfHaNoi')

    plt.xlabel('Kích cỡ chuỗi (length)')
    plt.ylabel('Thời gian (s)')

    plt.legend(loc='best') # thêm chú thích
    plt.show()

