import time
import matplotlib.pyplot as plt

# Đệ quy Fibonacci
def fibonacciRecursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2)

# Khử đệ quy fibonacci
def fibonacciEliminationRecursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        f0 = 1
        f1 = 1
        for i in range(2, number + 1):
            fn = f0 + f1 
            f0 = f1
            f1 = fn
        return fn


# Vẽ đồ thị thời gian so sánh
def data():
    nameTime = [1, 10, 100, 1000, 10000]
    listTimeRecursive = []
    listTimeEliminate = []
    for i in range(len(nameTime)):
        start1 = time.perf_counter_ns()
        fibonacciRecursive(nameTime[i])
        end1 = time.perf_counter_ns()
        spaceRecursive = end1 - start1
        listTimeRecursive.append(spaceRecursive)

        start2 = time.perf_counter_ns()
        fibonacciRecursive(nameTime[i])
        end2 = time.perf_counter_ns()
        spaceEliminate = end2 - start2
        listTimeEliminate.append(spaceEliminate)

    return nameTime, listTimeRecursive, listTimeEliminate


if __name__ == "__main__":
    nameTime, listTimeRecursive, listTimeEliminate = data()
    plt.plot(nameTime, listTimeRecursive, color='red', label='Recursive')
    plt.plot(nameTime, listTimeEliminate, color='green', label='Eliminate')
    plt.title('Biểu đồ thời gian chạy của thuật toán Fibonacci')

    plt.xlabel('Kích cỡ chuỗi (length)')
    plt.ylabel('Thời gian (s)')

    plt.legend(loc='best') # thêm chú thích
    plt.show()
