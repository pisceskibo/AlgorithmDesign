"""
Cho n tam giác trên mặt phẳng
Tam giác i bao tam giác j nếu 3 đỉnh tam giác j nằm trong tam giác i 
Tìm tam giác bao nhau có nhiều tam giác nhất
"""

def point_in_triangle(pt, tri):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1 = sign(pt, tri[0], tri[1]) < 0
    b2 = sign(pt, tri[1], tri[2]) < 0
    b3 = sign(pt, tri[2], tri[0]) < 0

    return (b1 == b2) and (b2 == b3)

def triangle_contains(t1, t2):
    return all(point_in_triangle(v, t1) for v in t2)

# Tìm dãy tam giác bao nhau dài nhất
def max_nested_triangles(triangles):
    n = len(triangles)
    dp = [1] * n  # Mảng dp để lưu độ dài dãy tối đa kết thúc tại mỗi tam giác

    # Sắp xếp tam giác theo tọa độ x nhỏ nhất của đỉnh
    triangles.sort(key=lambda x: min(v[0] for v in x))

    for i in range(n):
        for j in range(i):
            if triangle_contains(triangles[i], triangles[j]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp), dp

if __name__ == "__main__":
    triangles = [
        [(0, 0), (5, 0), (2.5, 5)],
        [(1, 1), (4, 1), (2.5, 4)],
        [(1, 1), (3, 1), (2, 3)],
        [(2, 2), (3, 2), (2.5, 2.5)]
    ]
    max_length, dp_array = max_nested_triangles(triangles)
    print(max_length)
    print(dp_array)