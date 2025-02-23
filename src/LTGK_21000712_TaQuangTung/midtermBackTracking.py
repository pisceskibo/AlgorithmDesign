def generate_combinations(n, k):
    # Mảng để lưu giữ tổ hợp hiện tại
    x = [0] * k

    lst = ["Hoa", "Mai", "Ngọc", "Lan", "Anh", "Đào"]

    def backtracking(i):
        # Điểm bắt đầu của j dựa trên phần tử cuối cùng của x[i - 1]
        start = x[i - 1] + 1 if i > 0 else 1
        # Điểm kết thúc của j dựa trên số phần tử còn lại cần phải chọn
        end = n - k + i + 1

        for j in range(start, end + 1):
            x[i] = j
            if i == k - 1:
                # Nếu đây là phần tử cuối cùng trong tổ hợp, in tổ hợp
                print(x)
                for m in x:
                    print(lst[m - 1], end = " ")
                
                print()
            else:
                # Nếu chưa đủ k phần tử, tiếp tục quay lui
                backtracking(i + 1)
        
    # Bắt đầu quá trình quay lui từ phần tử đầu tiên trong tổ hợp
    backtracking(0)

if __name__ == "__main__":
    n = 6
    k = 3
    generate_combinations(n, k)
