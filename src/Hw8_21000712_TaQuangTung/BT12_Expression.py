"""
(Expression) Cho n số nguyên. 
Hãy chia chúng thành 2 nhóm sao cho tích của tổng 2 nhóm là lớn nhất.
"""
from random import randrange

def expressionSplit(array):
    array.sort()
    sum1 = sum2 = 0

    arr1 = []
    arr2 = []

    for i in range(len(array)):
        if i < len(array) / 2:
            sum1 += array[i]
            arr1.append(array[i])
        else:
            sum2 += array[i]
            arr2.append(array[i])
    
    return arr1, arr2, sum1*sum2

if __name__ == "__main__":
    array = [randrange(1, 10) for _ in range(10)]
    grp1, grp2, maxSplit = expressionSplit(array)
    print("Group A là:", grp1)
    print("Group B là:", grp2)
    print("Tích lớn nhất của tổng là:", maxSplit)