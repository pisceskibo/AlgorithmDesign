from random import randrange
import time
import matplotlib.pyplot as plt

def max_meetings(start, end):
    # Tạo danh sách các cuộc họp với thời gian bắt đầu, kết thúc và chỉ số
    meetings = sorted((e, i) for i, (s, e) in enumerate(zip(start, end)))
    
    # Lựa chọn cuộc họp
    max_meetings = []
    last_end_time = 0
    
    for end_time, index in meetings:
        if start[index] >= last_end_time:
            max_meetings.append(index + 1)  # Lưu ý +1 vì chỉ số người dùng thường bắt đầu từ 1
            last_end_time = end_time
    
    return max_meetings

def randomStartEnd(size):
    startEndArray = []
    for length in size:
        temp = []
        tempStart = []
        tempEnd = []
        for element in range(length):
            tempStart.append(randrange(10))
        temp.append(tempStart)

        for element in range(length):
            tempEnd.append(randrange(10))
        temp.append(tempEnd)

        startEndArray.append(temp)
    return startEndArray

def getTime(X, Y):
    listTime = []
    for i in range(len(X)):
        time1 = time.perf_counter_ns()
        max_meetings(X[i], Y[i])
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ biểu đồ
def drawTime(nameXY, timeList):
    plt.plot(nameXY, timeList)
    plt.title("Biểu đồ thời gian bài toán xâu con chung")
    plt.xlabel("Name Array")
    plt.ylabel("Time (ns)")
    plt.show()


if __name__ == "__main__":
    # Ví dụ
    size = [5, 10, 100, 1000]
    start_times = [randomStartEnd(size)[i][0] for i in range(len(randomStartEnd(size)))]
    end_times = [randomStartEnd(size)[i][1] for i in range(len(randomStartEnd(size)))]

    listTime = getTime(start_times, end_times)
    drawTime(size, listTime)