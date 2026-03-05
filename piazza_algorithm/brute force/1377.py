# 백준 1377번
# 버블 소트

def change_frequency(arr):
    N = len(arr)
    moved = []
    indexed_arr = list(enumerate(arr))
    sorted_indexed_arr = sorted(indexed_arr, key=lambda x:x[1])
    
    for sorted_pos, (original_pos, value) in enumerate(sorted_indexed_arr):
        moved.append(original_pos - sorted_pos)
    
    print(max(moved) + 1)
    return 

N = int(input())
arr = []
arr.append(0)
for _ in range(N):
    arr.append(int(input()))

change_frequency(arr)

"""
(0,3) (1,1) (2,2) // 1
(1,1) (2,2) (0,3) // 1 1 -2
 1-0   2-1   0-2
"""