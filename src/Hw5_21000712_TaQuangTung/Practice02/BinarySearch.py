# Bài toán tìm kiếm nhị phân:
"""
1. Đặt bài toán:
Cho một mảng đã được sắp xếp và một giá trị key cần tìm, trả về chỉ số của key trong mảng nếu tồn tại, ngược lại trả về -1.

2. Phân tích bài toán:
Input: Một mảng đã được sắp xếp và một giá trị key.
Output: Chỉ số của key trong mảng hoặc -1 nếu key không tồn tại.

3. Thuật toán:
B1: So sánh key với phần tử ở giữa mảng.
B2: Nếu bằng, trả về chỉ số.
B3: Nếu key nhỏ hơn phần tử giữa, tìm kiếm nửa trái của mảng.
B4: Nếu key lớn hơn, tìm kiếm nửa phải của mảng.
B5: Nếu không tìm thấy, trả về -1.

4. Phân tích thuật toán:
+ Độ phức tạp thời gian: O(log n) vì mỗi lần chia mảng làm đôi.
+ Độ phức tạp không gian: O(1) trong trường hợp sử dụng tìm kiếm nhị phân lặp.
"""

def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1

# Ví dụ sử dụng
arr = [2, 3, 4, 10, 40]
key = 10
result = binary_search(arr, 0, len(arr) - 1, key)
print("Index of", key, "is", result)
