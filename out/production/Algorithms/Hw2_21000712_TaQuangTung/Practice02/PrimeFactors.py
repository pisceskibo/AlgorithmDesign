import time
import matplotlib.pyplot as plt

# Đệ quy
def primeFactorRecursive(n, factor=2, arrayPrimeFactor=None):
    if arrayPrimeFactor is None:
        arrayPrimeFactor = []
    
    # Điều kiện dừng: nếu n = 1, trả về danh sách các thừa số nguyên tố
    if n == 1:
        return arrayPrimeFactor
    # Nếu factor là một thừa số của n, chia n cho factor và lưu factor vào danh sách
    elif n % factor == 0:
        arrayPrimeFactor.append(factor)
        return primeFactorRecursive(n // factor, factor, arrayPrimeFactor)
    else:
        # Tăng factor và tiếp tục tìm kiếm thừa số tiếp theo
        return primeFactorRecursive(n, factor+1, arrayPrimeFactor)


# Khử đệ quy
def primeFactorEliminateRecursive(number):
    arrayPrimeFactor = []
    i = 2
    while (number > 1):
        while (number % i == 0):
            arrayPrimeFactor.append(i)
            number //= i
        i += 1
    return arrayPrimeFactor


# Vẽ đồ thị thời gian so sánh
def data():
    nameTime = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
    listTimeRecursive = []
    listTimeEliminate = []
    for i in range(len(nameTime)):
        start1 = time.perf_counter_ns()
        primeFactorRecursive(nameTime[i])
        end1 = time.perf_counter_ns()
        spaceRecursive = end1 - start1
        listTimeRecursive.append(spaceRecursive)

        start2 = time.perf_counter_ns()
        primeFactorEliminateRecursive(nameTime[i])
        end2 = time.perf_counter_ns()
        spaceEliminate = end2 - start2
        listTimeEliminate.append(spaceEliminate)

    return nameTime, listTimeRecursive, listTimeEliminate


if __name__ == "__main__":
    nameTime, listTimeRecursive, listTimeEliminate = data()
    plt.plot(nameTime, listTimeRecursive, color='red', label='Recursive')
    plt.plot(nameTime, listTimeEliminate, color='green', label='Eliminate')
    plt.title('Biểu đồ thời gian chạy của thuật toán PrimeFactors')

    plt.xlabel('Kích cỡ chuỗi (length)')
    plt.ylabel('Thời gian (s)')

    plt.legend(loc='best') # thêm chú thích
    plt.show()
