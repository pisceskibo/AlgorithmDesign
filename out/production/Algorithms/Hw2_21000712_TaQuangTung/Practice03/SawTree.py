# Khử đệ quy

n = int(input("Nhập số cây cần khai thác: "))
M = int(input("Nhập số mét cần khai thác: "))

LengthTree = []         # Mảng gồm chiều cao các cây tương ứng
for i in range(n):
    LengthTree.append(int(input(f"Nhập chiều cao cây thứ {i+1}: ")))
print("Mảng gồm độ dài các cây ban đầu là:", LengthTree)

MaxiumTree = max(LengthTree)


# Xử lý thuật toán
TreeKhaiThac = 0
mangIndex = []
Chenhlech = 0

while TreeKhaiThac < M:
    MaxTree = max(LengthTree)
    for tree in range(n):
        if LengthTree[tree] == MaxTree:
            LengthTree[tree] -= 1
            TreeKhaiThac += 1
    Chenhlech +=1
print("Số mét gỗ M tối thiểu cần khai thác là:", TreeKhaiThac)
print("Mảng gồm độ dài các cây lúc sau khi cưa là:", LengthTree)
print("Giá trị h cần tìm là:", MaxiumTree - Chenhlech)
