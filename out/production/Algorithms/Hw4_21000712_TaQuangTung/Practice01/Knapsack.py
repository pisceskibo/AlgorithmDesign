# Bài toán xếp balo (0-1)
arrayItems = [5, 3, 2, 4]
arrayMoney = [10, 5, 3, 6]
maxWeight = 27

i = 0
count = 0
numberOfItems = []
while i < len(arrayItems):
    currentItem = arrayItems[i] * arrayMoney[i]
    maxWeight -= currentItem

    if maxWeight >= 0:
        count += 1
    else:
        maxWeight += currentItem
        numberOfItems.append(count)
        count = 0
        i += 1
print(numberOfItems)
