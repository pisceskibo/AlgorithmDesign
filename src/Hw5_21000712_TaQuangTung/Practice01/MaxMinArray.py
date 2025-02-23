from random import randrange
import time
import matplotlib.pyplot as plt

# Tìm phần tử lớn nhất và nhỏ nhất trong mảng
def findMax(arr, left, right):
    if (left == right):
        return arr[right]
    else:
        max1 = findMax(arr, left, (left + right)//2)
        max2 = findMax(arr, (left + right)//2 + 1, right)
        return max1 if (max1 > max2) else max2

def findMin(arr, left, right):
    if (left == right):
        return arr[left]
    else:
        min1 = findMin(arr, left, (left + right)//2)
        min2 = findMin(arr, (left + right)//2 + 1, right)
        return min1 if (min1 > min2) else min2
    
def timeList(sizeArray, listArraySize):
    timeListMax = []
    timeListMin = []

    for i in range(len(sizeArray)):
        # Mảng thời gian max
        time1 = time.perf_counter_ns()
        findMax(listArraySize[i], 0, len(listArraySize[i]) - 1)
        time2 = time.perf_counter_ns()
        timeListMax.append(time2 - time1)

        # Mảng thời gian min
        time3 = time.perf_counter_ns()
        findMin(listArraySize[i], 0, len(listArraySize[i]) - 1)
        time4 = time.perf_counter_ns()
        timeListMin.append(time4 - time3)

    return timeListMax, timeListMin


# Vẽ đồ thị
def drawTime(sizeArray, timeListMax, timeListMin):
    plt.plot(sizeArray, timeListMax)
    plt.plot(sizeArray, timeListMin)
    plt.title("Biểu đồ thời gian toán tìm min - max")
    plt.xlabel("Size Array")
    plt.ylabel("Time (ns)")

if __name__ == "__main__":
    sizeArray = [10, 100, 1000, 10000]
    listArraySize = []
    for size in sizeArray:
        values = []
        for i in range(size):
            value = randrange(100)
            values.append(value)
        listArraySize.append(values)

    timeListMax, timeListMin = timeList(sizeArray, listArraySize)
    print(timeListMax)
    print(timeListMin)
    drawTime(sizeArray, timeListMax, timeListMin)
    plt.show()