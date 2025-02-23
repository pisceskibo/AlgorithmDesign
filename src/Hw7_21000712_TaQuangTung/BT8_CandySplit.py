"""
Cho n gói kẹo, gói thứ i có ai viên. 
Hãy chia các gói thành 2 phần sao cho chênh lệch giữa 2 phần là ít nhất.
"""

from random import randrange

def candy_split(candies):
    n = len(candies)
    total_sum = sum(candies)
    
    # Cơ sở quy hoạch động
    dp = [[False] * (total_sum // 2 + 1) for _ in range(n + 1)]
    dp[0][0] = True 
    decision = [[False] * (total_sum // 2 + 1) for _ in range(n + 1)]
    
    # Quy hoạch động
    for i in range(1, n + 1):
        for j in range(total_sum // 2 + 1):
            if j >= candies[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - candies[i - 1]]
                if dp[i][j] and dp[i - 1][j - candies[i - 1]]:
                    decision[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Tìm nghiệm tối ưu
    for i in range(total_sum // 2, -1, -1):
        if dp[n][i]:
            part1 = i
            break
    
    # Truy vết tìm nghiệm
    part1_candies = []
    w = part1
    for i in range(n, 0, -1):
        if decision[i][w]:
            part1_candies.append(candies[i - 1])
            w -= candies[i - 1]

    part2_candies = list(candies)
    for candy in part1_candies:
        part2_candies.remove(candy)

    return part1_candies, part2_candies

if __name__ == "__main__":
    candyArray = [randrange(10) for _ in range(10)]
    part1, part2 = candy_split(candyArray)
    print("Phần 1:", part1)
    print("Phần 2:", part2)
