import random

# 선택 정렬
def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            min_idx = j if arr[j] < arr[min_idx] else min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 랜덤 1000개 숫자 리스트 생성 (범위: 1~5000)
arr = []
for i in range(1000):
    arr.append(random.randint(1, 5000))
sorted_arr = selection_sort(arr)

print(sorted_arr)