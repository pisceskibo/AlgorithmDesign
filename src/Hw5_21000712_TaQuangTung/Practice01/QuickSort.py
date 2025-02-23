from random import randrange
import time
import matplotlib.pyplot as plt

# Tìm vị trí
def partition(array, low, high):
	# Chọn phần tử phải nhất làm trục
	pivot = array[high]

	# Trỏ vào phần tử lớn hơn
	i = low - 1

    # Duyệt tất cả các phần tử và so sánh với trục
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Hoán đổi phần tử trụ với phần tử lớn hơn được chỉ định bởi i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1


def quickSort(array, low, high):
	if low < high:
        # Tìm phần tử trục sao cho phần tử nhỏ hơn nằm bên trái, lớn hơn bên phải
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)

def randomElement(arraySize):
	arrayValue = []
	for size in arraySize:
		arrayTemp = []
		for i in range(size):
			arrayTemp.append(randrange(-100, 100))
		arrayValue.append(arrayTemp)
	return arrayValue

def getTime(arrayValue):
	listTime = []
	for elementArray in arrayValue:
		time1 = time.perf_counter_ns()
		quickSort(elementArray, 0, len(elementArray) - 1)
		time2 = time.perf_counter_ns()
		listTime.append(time2 - time1)
	return listTime

# Vẽ đồ thị
def drawTime(sizeArray, timeList):
    plt.plot(sizeArray, timeList)
    plt.title("Biểu đồ thời gian thuật toán Quick Sort")
    plt.xlabel("Size Array")
    plt.ylabel("Time (ns)")
    plt.show()


if __name__ == "__main__":
	arraySize = [5, 10, 50, 100, 500, 1000]
	arrayValue = randomElement(arraySize)    
	listTime = getTime(arrayValue)
	drawTime(arraySize, listTime)
