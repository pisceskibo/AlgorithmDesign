# Bài toán lập lịch sử dụng tài nguyên
import time
import matplotlib.pyplot as plt

# Hàm xử lý thuật toán
def activity_selection(activities):
    # Sắp xếp các hoạt động theo thời gian kết thúc tăng dần
    activities.sort(key=lambda x: x[1])
    
    # Chọn hoạt động đầu tiên và thêm vào lịch trình
    selected_activities = [activities[0]]
    
    # Duyệt qua các hoạt động còn lại và chọn hoạt động không xung đột
    for i in range(1, len(activities)):
        # Nếu thời gian bắt đầu của hoạt động hiện tại lớn hơn hoặc bằng thời gian kết thúc của hoạt động cuối cùng được chọn, thêm vào lịch trình
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])
    
    return selected_activities


# Hàm lấy thời gian
def getTime(activities):
    listTime = []
    for element in activities:
        time1 = time.perf_counter_ns()
        selected_activities = activity_selection(element)
        time2 = time.perf_counter_ns()
        listTime.append(time2 - time1)
    return listTime

# Vẽ dữ liệu thời gian
def drawTime(sizeList, timeList):
    plt.plot(sizeList, timeList)
    plt.title("Biểu đồ thời gian bài toán xếp lịch")
    plt.xlabel("Size")
    plt.ylabel("Time (ns)")

    plt.show()

if __name__ == "__main__":
    # Danh sách các hoạt động, mỗi hoạt động được biểu diễn dưới dạng một cặp (thời gian bắt đầu, thời gian kết thúc)
    activities1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10)]
    activities2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
    activities3 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12)]
    activities4 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14)]
    activities5 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

    activities = [activities1, activities2, activities3, activities4, activities5]
 
    # Gọi hàm và in kết quả
    timeList = getTime(activities)
    sizeList = [len(activities1), len(activities2), len(activities3), len(activities4), len(activities5)]
    drawTime(sizeList, timeList)