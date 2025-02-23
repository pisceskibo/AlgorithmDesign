"""
Dãy Wavio là dãy tăng đến 1 đỉnh và giảm từ đỉnh đó
"""

def wavioArray(array):
    n = len(array)

    # Chạy vòng lặp từ phần tử đầu tiên đến phần tử áp chót trong mảng
    for start_index in range(n):
        for peak_index in range(start_index + 1, n - 1):
            increase = []
            decrease = []

            # Xây dựng dãy tăng đến đỉnh
            if array[start_index] < array[start_index + 1]:
                increase.append(array[start_index])
            for j in range(start_index + 1, peak_index + 1):
                if len(increase) == 0 or (array[j] > increase[-1]):
                    increase.append(array[j])

            # Xây dựng dãy giảm từ đỉnh
            if len(increase) > 0 and array[peak_index + 1] < increase[-1]:
                decrease.append(array[peak_index + 1])
            for j in range(peak_index + 2, n):
                if len(decrease) == 0 or (array[j] < decrease[-1]):
                    decrease.append(array[j])

            # Nếu có dãy tăng và giảm, in ra kết quả
            if len(increase) > 1 and len(decrease) > 0:
                print(f"Wavio sequence from index {start_index} to {n-1}:", increase + decrease)


if __name__ == "__main__":
    array = [1, 2, 3, 8, 9, 6, 5, 4, 0]
    wavioArray(array)
