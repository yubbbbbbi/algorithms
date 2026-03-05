import random

# 버블 정렬
def bubble_sort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 랜덤 1000개 숫자 리스트 생성 (범위: 1~5000)
arr = []
for i in range(1000):
    arr.append(random.randint(1, 5000))

sorted_arr = bubble_sort(arr)
print(sorted_arr)