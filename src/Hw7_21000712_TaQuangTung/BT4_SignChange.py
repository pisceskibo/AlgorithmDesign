"""
Cho dãy A1 --> An. Tìm dãy con đổi dấu dài nhất của dãy đó:
+ Ai1 < Ai2 > Ai3 < ... hoặc Ai1 > Ai2 < Ai3 > ...
+ Các chỉ số phải cách nhau ít nhất L: i2 − i1 ≥ L, i3 − i2 ≥ L, ...
+ Chênh lệch giữa 2 phần tử liên tiếp nhỏ hơn U
"""

def longest_alternating_subsequence(N, A, L, U):
    # Khởi tạo mảng dp
    dp_up = [1] * N
    dp_down = [1] * N
    
    # Kết quả lớn nhất
    max_length = 1

    # Tính toán các giá trị dp
    for i in range(N):
        for j in range(i + L, N):
            if j - i >= L and abs(A[i] - A[j]) <= U:
                if A[i] < A[j]:
                    dp_up[j] = max(dp_up[j], dp_down[i] + 1)
                elif A[i] > A[j]:
                    dp_down[j] = max(dp_down[j], dp_up[i] + 1)
        
        # Cập nhật kết quả lớn nhất
        max_length = max(max_length, dp_up[i], dp_down[i])

    return max_length

if __name__ == "__main__":
    A = [1, 7, 5, 9, 2, 5, 3]
    N = len(A)
    L = 2
    U = 8
    print(longest_alternating_subsequence(N, A, L, U))
