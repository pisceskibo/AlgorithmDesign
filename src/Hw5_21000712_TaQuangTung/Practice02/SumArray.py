# Tính tổng các phần tử trong mảng:
"""
1. Đặt bài toán:
Cho một mảng các số, tính tổng của tất cả các phần tử trong mảng.

2. Phân tích bài toán:
Input: Một mảng số.
Output: Tổng của các phần tử trong mảng.

3. Thuật toán:
B1: Nếu mảng chỉ có một phần tử, trả về phần tử đó.
B2: Chia mảng thành hai nửa.
B3: Tính tổng của nửa trái và nửa phải sử dụng đệ quy.
B4: Cộng tổng của hai nửa lại với nhau.

4. Phân tích thuật toán:
+ Độ phức tạp thời gian: O(n) vì mỗi phần tử được xử lý một lần.
+ Độ phức tạp không gian: O(log n) vì độ sâu của stack đệ quy là log n.
"""

def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_sum = sum_array(arr[:mid])
        right_sum = sum_array(arr[mid:])
        return left_sum + right_sum

# Ví dụ sử dụng
arr = [1, 2, 3, 4, 5]
result = sum_array(arr)
print("Sum of array is", result)
