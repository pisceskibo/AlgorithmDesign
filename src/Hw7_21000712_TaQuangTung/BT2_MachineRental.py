"""
Trung tâm tính toán hiệu năng cao nhận được của n khách hàng
Khách hàng i sử dụng máy trong khoảng thời gian [ai, bi] và trả tiền thuê ci
Bố trí lịch thuê máy để tổng số tiền thu được là max mà thời gian sử dụng máy của 2 khách không giao nhau
"""

def calculate_max_revenue(orders):
    # Sắp xếp các cuộc họp theo thứ tự kết thúc tăng dần
    sortedOrders = sorted(orders, key=lambda order: order[1])

    n = len(sortedOrders)
    revenue = [0] * n  # Mảng chứa doanh thu
    parent = [-1] * n  # Mảng truy vết
    
    # Lữu trữ giá tiền
    cost = [order[2] for order in sortedOrders]

    for i in range(n):
        revenue[i] = cost[i]

        # Kiểm tra điều kiện
        for j in range(i):
            if sortedOrders[j][1] <= sortedOrders[i][0]:  
                # revenue[i] = max(revenue[i], revenue[j] + cost[i])
                if revenue[i] < revenue[j] + cost[i]:
                    revenue[i] = revenue[j] + cost[i]
                    parent[i] = j

    # Tìm giá trị doanh thu tối đa
    max_revenue = max(revenue)
    max_index = revenue.index(max_revenue)

    # Truy vết các yêu cầu được chọn
    optimal_orders = []
    while max_index != -1:
        optimal_orders.append(sortedOrders[max_index])
        max_index = parent[max_index]

    optimal_orders.reverse()

    return max_revenue, optimal_orders


if __name__ == "__main__":
    orders = [(1, 4, 10), (3, 5, 12), (2, 7, 18), (0, 6, 15)]

    max_revenue = calculate_max_revenue(orders)
    print("Maximum revenue:", max_revenue)
