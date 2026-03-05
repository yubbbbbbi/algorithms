# 백준 23881번
# 알고리즘 수업 - 선택 정렬 1

def get_selection_sort_switched_number(arr, K):
    N = len(arr)
    count = 0
    for i in range(N-1, -1, -1):
        max_idx = i
        for j in range(i):
            max_idx = j if arr[j] > arr[max_idx] else max_idx
        if max_idx == i:
            continue
        num_big = arr[max_idx]
        num_small = arr[i]
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
        count += 1
        if count == K:
            print(num_small, num_big)
            return 
    print("-1")
    return

_, K = map(int, input().split())
arr = list(map(int, input().split()))

get_selection_sort_switched_number(arr, K)