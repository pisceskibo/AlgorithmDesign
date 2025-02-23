import numpy as np
import time
import matplotlib.pyplot as plt

# Cộng ma trận
def addMatrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Trừ ma trận
def substractMatrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# Nhân hai ma trận
def splitMatrix(matrix, n):
    row, col = n, n
    mid_row, mid_col = row // 2, col // 2

    # Tách thành 4 ma trận con góc
    C11 = [row[:mid_col] for row in matrix[:mid_row]]
    C12 = [row[mid_col:] for row in matrix[:mid_row]]
    C21 = [row[:mid_col] for row in matrix[mid_row:]]
    C22 = [row[mid_col:] for row in matrix[mid_row:]]
    return C11, C12, C21, C22

def combineMatrix(C11, C12, C21, C22):
    # Ghép nửa trên của ma trận
    top_half = [C11_row + C12_row for C11_row, C12_row in zip(C11, C12)]
    # Ghép nửa dưới của ma trận
    bottom_half = [C21_row + C22_row for C21_row, C22_row in zip(C21, C22)]
    # Kết hợp nửa trên và nửa dưới lại với nhau
    return top_half + bottom_half


def multiplyMatrix(A, B, n):
    if (n == 1):
        return [[A[0][0] * B[0][0]]]
    else:
        A11, A12, A21, A22 = splitMatrix(A, n)
        B11, B12, B21, B22 = splitMatrix(B, n)

        X1 = multiplyMatrix(A11, B11, n//2)
        X2 = multiplyMatrix(A12, B21, n//2)
        C11 = addMatrix(X1, X2)
    
        X3 = multiplyMatrix(A11, B12, n//2)
        X4 = multiplyMatrix(A12, B22, n//2)
        C12 = addMatrix(X3, X4)

        X5 = multiplyMatrix(A21, B11, n//2)
        X6 = multiplyMatrix(A22, B21, n//2)
        C21 = addMatrix(X5, X6)

        X7 = multiplyMatrix(A21, B12, n//2)
        X8 = multiplyMatrix(A22, B22, n//2)
        C22 = addMatrix(X7, X8)

        return combineMatrix(C11, C12, C21, C22)


def strassen(A, B, n):
    if (n == 1):
        return [[A[0][0] * B[0][0]]]
    else:
        A11, A12, A21, A22 = splitMatrix(A, n)
        B11, B12, B21, B22 = splitMatrix(B, n)

        P1 = strassen(A11, substractMatrix(B12, B22), n//2)
        P2 = strassen(addMatrix(A11, A12), B22, n//2)
        P3 = strassen(addMatrix(A21, A22), B11, n//2)
        P4 = strassen(A22, substractMatrix(A21, B11), n//2)
        P5 = strassen(addMatrix(A11, A22), addMatrix(B11, B22), n//2)
        P6 = strassen(substractMatrix(A12, A22), addMatrix(B21, B22), n//2)
        P7 = strassen(substractMatrix(A11, A21), addMatrix(B11, B12), n//2)

        C11 = addMatrix(substractMatrix(addMatrix(P5, P4), P2), P6)
        C12 = addMatrix(P1, P2)
        C21 = addMatrix(P4, P3)
        C22 = substractMatrix(substractMatrix(addMatrix(P1, P5), P3), P7)

        return combineMatrix(C11, C12, C21, C22)
    
def timeList(sizeArray, matrixList):
    timeListDivide = []
    timeListStrassen = []

    for i in range(len(sizeArray)):
        # Mảng thời gian max
        time1 = time.perf_counter_ns()
        multiplyMatrix(matrixList[i][0], matrixList[i][1], sizeArray[i])
        time2 = time.perf_counter_ns()
        timeListDivide.append(time2 - time1)

        # Mảng thời gian min
        time3 = time.perf_counter_ns()
        strassen(matrixList[i][0], matrixList[i][1], sizeArray[i])
        time4 = time.perf_counter_ns()
        timeListStrassen.append(time4 - time3)

    return timeListDivide, timeListStrassen

# Vẽ đồ thị
def drawTime(sizeArray, timeListDivide, timeListStrassen):
    plt.plot(sizeArray, timeListDivide)
    plt.plot(sizeArray, timeListStrassen)
    plt.title("Biểu đồ thời gian toán nhân ma trận")
    plt.xlabel("Size Array")
    plt.ylabel("Time (ns)")
    plt.show()


if __name__ == "__main__":
    matrixA1 = np.random.randint(0, 10, (2, 2)).tolist()
    matrxiB1 = np.random.randint(0, 10, (2, 2)).tolist()
    
    matrxiA2 = np.random.randint(0, 10, (4, 4)).tolist()
    matrxiB2 = np.random.randint(0, 10, (4, 4)).tolist()
    
    matrxiA3 = np.random.randint(0, 10, (8, 8)).tolist()
    matrxiB3 = np.random.randint(0, 10, (8, 8)).tolist()
    
    sizeArray = [2, 4, 8]
    matrixList = [[matrixA1, matrxiB1], [matrxiA2, matrxiB2], [matrxiA3, matrxiB3]]
    timeListDivide, timeListStrassen = timeList(sizeArray, matrixList)

    drawTime(sizeArray, timeListDivide, timeListStrassen)
    # print("1. Nhân ma trận theo phương pháp chia để trị:")
    # result1 = multiplyMatrix(A, B, n)
    # for row in result1:
    #     print(row)

    # print("2. Nhân hai ma trận theo thuật toán Strassen:")
    # result2 = multiplyMatrix(A, B, n)
    # for row in result2:
    #     print(row)