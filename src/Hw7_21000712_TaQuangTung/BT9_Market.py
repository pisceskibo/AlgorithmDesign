"""
Người đánh cá bắt n con cá, khối lượng mỗi con là ai
Bán cá theo khối lượng: 3kg, 5kg, ...
"""
from random import randrange

def counter_fishers(weightFishes):
    total_sum = sum(weightFishes)
    
    # Cơ sở quy hoạch động
    dp = [False] * (total_sum + 1)
    dp[0] = True  # Có thể đạt tổng bằng 0 với 0 con cá
    
    # Mảng để truy vết các con cá đã chọn
    parent = [-1] * (total_sum + 1)
    
    # Quy hoạch động
    for i, weight in enumerate(weightFishes):
        for j in range(total_sum, weight - 1, -1):
            if not dp[j] and dp[j - weight]:
                dp[j] = True
                parent[j] = i
    
    # Nghiệm tối ưu
    possible_weights = [i for i in range(1, total_sum + 1) if dp[i]]
    
    # Truy vết các con cá đã chọn cho từng khối lượng khả thi
    weight_to_fishes = {}
    for weight in possible_weights:
        trace = []
        current_weight = weight
        while current_weight > 0:
            fish_index = parent[current_weight]
            trace.append(weightFishes[fish_index])
            current_weight -= weightFishes[fish_index]
        weight_to_fishes[weight] = trace
    
    return possible_weights, weight_to_fishes

if __name__ == "__main__":
    weightFishes = [randrange(1, 10) for _ in range(5)]  # Tạo danh sách khối lượng ngẫu nhiên từ 1 đến 10
    possible_weights, weight_to_fishes = counter_fishers(weightFishes)
    print("Khối lượng các con cá:", weightFishes)
    print("Số lượng các khối lượng có thể mua là:", len(possible_weights))
    print("Các khối lượng có thể mua là:", possible_weights)
    for weight in possible_weights:
        print(f"Khối lượng {weight} kg có thể được tạo từ các con cá:", weight_to_fishes[weight])
