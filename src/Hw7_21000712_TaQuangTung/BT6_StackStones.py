"""
Các khối đá HCN có 3 kích thước: dài, rộng cao (cao = min)
Các khối được đặt song song sao cho không có phần nào khối trên nằm chìa ra khối dưới
=> Tìm cách xếp nhiều khối đá nhất
"""

def max_tower(blocks):
    # Sinh ra tất cả cách đặt cho mỗi khối đá
    all_orientations = []
    for block in blocks:
        length, width, height = block
        # Thêm các hoán vị có thể của chiều dài, rộng và cao
        all_orientations.append((length, width, height))
        all_orientations.append((length, height, width))
        all_orientations.append((width, length, height))
        all_orientations.append((width, height, length))
        all_orientations.append((height, length, width))
        all_orientations.append((height, width, length))

    # Sắp xếp các khối theo diện tích đáy giảm dần, nếu diện tích bằng nhau thì theo chiều cao giảm dần
    all_orientations.sort(key=lambda x: (x[0] * x[1], x[2]), reverse=True)

    # Quy hoạch động để tìm số lượng khối tối đa
    n = len(all_orientations)
    dp = [1] * n  # Mỗi khối ít nhất có thể xếp một mình

    for i in range(n):
        for j in range(i):
            # Kiểm tra khối j có thể xếp dưới khối i không
            if (all_orientations[j][0] >= all_orientations[i][0] and all_orientations[j][1] >= all_orientations[i][1]) or \
               (all_orientations[j][1] >= all_orientations[i][0] and all_orientations[j][0] >= all_orientations[i][1]):
                # Nếu khối j có thể xếp dưới khối i, cập nhật dp[i]
                dp[i] = max(dp[i], dp[j] + 1)

    # Trả về số lượng khối tối đa có thể xếp chồng lên nhau
    return max(dp)

if __name__ == "__main__":
    blocks = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    print(max_tower(blocks))
