# 백준 23882번
# 알고리즘 수업 - 선택 정렬 2

def selection_sort(arr, K):
    N = len(arr)
    count = 0
    for i in range(N-1, -1, -1):
        max_idx = i
        for j in range(i):
            max_idx = j if arr[j] > arr[max_idx] else max_idx
        if max_idx == i:
            continue
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        count += 1
        if count == K:
            return arr
    return -1

_, K = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = selection_sort(arr, K)
if sorted_arr == -1:
    print("-1")
else:
    for i in range(len(sorted_arr)):
        print(sorted_arr[i], end=" ")
