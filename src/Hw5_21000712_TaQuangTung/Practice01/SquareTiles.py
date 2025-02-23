import time
import matplotlib.pyplot as plt

"""
board: bảng biểu diễn trạng thái
top, left: chỉ số hàng và cột tại góc trên bên trái của phần bàn cờ hiện
dr, dc: tọa độ dòng và cột của ô thoát nước
"""

# Chia thành 4 phần bằng nhau
def tile(board, top, left, dr, dc, size):
    # Tọa độ cho gạch hình chữ L trung tâm [(0, 0), (0, 1), (1, 0), (1, 1)]
    if size == 1:
        return
    
    # Tìm vị trí trung tâm của bàn cờ hiện tại
    s = size // 2

    # Xác định phần chứa ô thoát nước
    for i in range(4):
        # Kích cỡ sau khi chia thành 4 phần nhỏ hơn
        r = top + (i // 2) * s
        c = left + (i % 2) * s
        if r <= dr < r + s and c <= dc < c + s:     # Kiểm tra ô thoát nước có nằm trong vùng đang xét không
            tile(board, r, c, dr, dc, s)
        else:
            # Đặt gạch hình chữ L
            nr = top + s - 1 + (i // 2)
            nc = left + s - 1 + (i % 2)
            board[nr][nc] = 'L'
    
    # Gọi đệ quy cho mỗi phần
    for i in range(4):
        nr = top + (i // 2) * s
        nc = left + (i % 2) * s
        if nr != top + s - 1 or nc != left + s - 1:
            tile(board, nr, nc, top + s - 1, left + s - 1, s)

# Vẽ đồ thị
def drawTime(sizeArray, timeList):
    plt.plot(sizeArray, timeList)
    plt.title("Biểu đồ thời gian bài toán lát gạch chữ L")
    plt.xlabel("Size Array")
    plt.ylabel("Time (ns)")
    plt.show()



if __name__ == "__main__":
    # Thiết lập bàn cờ và kích thước
    sizeList = [1, 2, 3, 4, 5, 6]
    timeList = []
    for n in sizeList:
        size = 2 ** n
        board = [['-' for _ in range(size)] for _ in range(size)]

        # Vị trí của ô thoát nước
        dr, dc = 1, 1  # Giả sử ô thoát nước ở (1, 1)

        # Đánh dấu ô thoát nước và bắt đầu lát gạch
        board[dr][dc] = 'W'
        time1 = time.perf_counter_ns()
        tile(board, 0, 0, dr, dc, size)
        time2 = time.perf_counter_ns()
        timeList.append(time2 - time1)

    drawTime(sizeList, timeList)