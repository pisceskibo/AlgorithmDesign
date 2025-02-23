# Đệ quy

n = int(input("Nhập số cây cần khai thác: "))
M = int(input("Nhập số mét cần khai thác: "))

LengthTree = []         # Mảng gồm chiều cao các cây tương ứng
for i in range(n):
    LengthTree.append(int(input(f"Nhập chiều cao cây thứ {i+1}: ")))
print("Mảng gồm độ dài các cây ban đầu là:", LengthTree)

MaxiumTree = max(LengthTree)

def woodAmount(height, trees):
    # Tính tổng lượng gỗ thu được nếu cắt các cây ở độ cao cho trước
    return sum(tree - height if tree > height else 0 for tree in trees)

def findHeight(low, high, trees, M):
    # Tìm giá trị h thích hợp bằng cách đệ quy
    if low > high:
        return high  # Khi không còn khả năng tìm kiếm, trả về giá trị cao nhất thỏa mãn

    mid = (low + high) // 2
    wood = woodAmount(mid, trees)
    
    if wood < M:  
        # Nếu lượng gỗ không đủ, thử với độ cao thấp hơn
        return findHeight(low, mid - 1, trees, M)
    else:  
        # Nếu lượng gỗ đủ hoặc dư, thử với độ cao cao hơn
        return findHeight(mid + 1, high, trees, M)

# Giả định rằng LengthTree và M đã được nhập như ở trên
maxHeight = max(LengthTree)
optimalHeight = findHeight(0, maxHeight, LengthTree, M)
print("Giá trị h thích hợp nhất là:", optimalHeight)
