# 백준 1377번
# 숫자 카드
# 이진탐색

import bisect

def is_exist(arr, target):
    idx = bisect.bisect_left(arr, target) # 이진탐색
    if idx < len(arr) and arr[idx] == target:
        return 1
    else:
        return 0
            
N = int(input())
card_list = sorted(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    print(is_exist(card_list, target_list[i]), end=" ")