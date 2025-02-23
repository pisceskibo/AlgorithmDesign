"""
Có n cuộc họp, cuộc họp i bắt đầu từ A[i] --> B[i]
"""


def schedule_meetings(meetings):
    # Sắp xếp các cuộc họp theo thứ tự kết thúc tăng dần
    sorted_meetings = sorted(meetings, key=lambda meeting: meeting[1])

    # Mảng để lưu thời gian bắt đầu và kết thúc của các cuộc họp sau khi sắp xếp
    A = [meeting[0] for meeting in sorted_meetings]
    B = [meeting[1] for meeting in sorted_meetings]

    # Khởi tạo bảng lưu trữ số lượng cuộc họp liên tiếp tối đa có thể có và người tiền nhiệm
    L = [1] * len(sorted_meetings)
    P = [-1] * len(sorted_meetings)  # Người tiền nhiệm trong chuỗi tối ưu

    # Tính toán độ dài chuỗi tối đa và truy vết người tiền nhiệm
    for i in range(len(sorted_meetings)):
        for j in range(i):
            if A[i] >= B[j] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
                P[i] = j

    # Tìm chỉ số cuộc họp có chuỗi tối đa và in chuỗi đó
    max_len = max(L)
    max_index = L.index(max_len)

    # Truy vết để tìm chuỗi
    optimal_sequence = []
    while max_index != -1:
        optimal_sequence.append(sorted_meetings[max_index])
        max_index = P[max_index]

    # Đảo ngược chuỗi để có trật tự từ đầu đến cuối
    optimal_sequence.reverse()

    print("Sorted Meetings:", sorted_meetings)
    print("Maximum length of non-overlapping meetings:", max_len)
    print("Optimal sequence of meetings:", optimal_sequence)

if __name__ == "__main__":
    meetings = [(1, 4), (3, 5), (0, 6), (5, 8), (4, 9), (7, 10)]
    schedule_meetings(meetings)
