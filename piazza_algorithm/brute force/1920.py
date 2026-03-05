# 백준 1920번
# 수 찾기
# 이진탐색

import bisect

def is_exit(list, target):
    idx = bisect.bisect_left(list, target)
    if idx < len(list) and list[idx] == target:
        return 1
    else:
        return 0

N = int(input())
num_list = sorted(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    print(is_exit(num_list, target_list[i]))