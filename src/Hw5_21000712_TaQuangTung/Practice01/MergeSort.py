from random import randrange
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Tìm chỉ số giữa của mảng
        left_half = arr[:mid]  # Chia mảng thành nửa trái
        right_half = arr[mid:]  # Chia mảng thành nửa phải

        merge_sort(left_half)  # Sắp xếp đệ quy nửa trái
        merge_sort(right_half)  # Sắp xếp đệ quy nửa phải

        # Trộn hai nửa đã được sắp xếp
        i = j = k = 0  # Khởi tạo chỉ mục
        # Trộn cho đến khi một trong hai nửa hết phần tử
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Sao chép các phần tử còn lại của nửa trái, nếu có
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Sao chép các phần tử còn lại của nửa phải, nếu có
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


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
		merge_sort(elementArray)
		time2 = time.perf_counter_ns()
		listTime.append(time2 - time1)
	return listTime

# Vẽ đồ thị
def drawTime(sizeArray, timeList):
    plt.plot(sizeArray, timeList)
    plt.title("Biểu đồ thời gian thuật toán Merge Sort")
    plt.xlabel("Size Array")
    plt.ylabel("Time (ns)")
    plt.show()


if __name__ == "__main__":
	arraySize = [5, 10, 50, 100, 500, 1000]
	arrayValue = randomElement(arraySize)    
	listTime = getTime(arrayValue)
	drawTime(arraySize, listTime)
