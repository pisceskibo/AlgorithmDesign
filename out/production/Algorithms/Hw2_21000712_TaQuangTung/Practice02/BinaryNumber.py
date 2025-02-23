import time
import matplotlib.pyplot as plt

# Đệ quy số nhị phân
def binaryRecursive(number):
    if number <= 0:
        return ""
    else:
        return binaryRecursive(number // 2) + str(number % 2)
    
# Khử đệ quy nhị phân
def binaryEliminateRecursion(number):
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


# Vẽ đồ thị thời gian so sánh
def data():
    nameTime = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
    listTimeRecursive = []
    listTimeEliminate = []
    for i in range(len(nameTime)):
        start1 = time.perf_counter_ns()
        binaryRecursive(nameTime[i])
        end1 = time.perf_counter_ns()
        spaceRecursive = end1 - start1
        listTimeRecursive.append(spaceRecursive)

        start2 = time.perf_counter_ns()
        binaryEliminateRecursion(nameTime[i])
        end2 = time.perf_counter_ns()
        spaceEliminate = end2 - start2
        listTimeEliminate.append(spaceEliminate)

    return nameTime, listTimeRecursive, listTimeEliminate


if __name__ == "__main__":
    nameTime, listTimeRecursive, listTimeEliminate = data()
    plt.plot(nameTime, listTimeRecursive, color='red', label='Recursive')
    plt.plot(nameTime, listTimeEliminate, color='green', label='Eliminate')
    plt.title('Biểu đồ thời gian chạy của thuật toán Binary Number')

    plt.xlabel('Kích cỡ chuỗi (length)')
    plt.ylabel('Thời gian (s)')

    plt.legend(loc='best') # thêm chú thích
    plt.show()
