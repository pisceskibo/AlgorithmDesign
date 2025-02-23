"""
Cho dãy A1, A2, ..., AN. Tìm một dãy con của dãy đó có tổng bằng S
"""

def find_subarray(A, S):
    n = len(A)
    dp = [[False for _ in range(S + 1)] for _ in range(n)]

    # Khởi tạo bảng dp
    for i in range(n):
        dp[i][0] = True
    for s in range(1, S + 1):
        dp[0][s] = (A[0] == s)  # Chỉnh sửa điều kiện khởi tạo cho phần tử đầu tiên

    # Duyệt bảng dp
    for i in range(1, n):
        for s in range(1, S + 1):
            if A[i] <= s:
                dp[i][s] = dp[i - 1][s] or dp[i - 1][s - A[i]]
            else:
                dp[i][s] = dp[i - 1][s]

    if not dp[n - 1][S]:
        return False, []  # Không tìm thấy dãy con nào thỏa mãn

    # Truy vết tìm các phần tử của dãy con
    result = []
    i, s = n - 1, S
    while s > 0:
        if i == 0:
            if dp[i][s]:
                result.append(A[i])
            break
        if dp[i - 1][s]:  # Nếu tổng S có thể đạt được mà không cần A[i]
            i -= 1
        else:  # Tổng S chỉ có thể đạt được bởi việc thêm A[i]
            result.append(A[i])
            s -= A[i]
            i -= 1

    result.reverse()
    return True, result

if __name__ == "__main__":
    A = [1, 2, 4, 5, 6]
    S = 12
    found, subarray = find_subarray(A, S)
    if found:
        print("Tìm thấy dãy con có tổng bằng", S, ":", subarray)
    else:
        print("Không tìm thấy dãy con nào thỏa mãn")
