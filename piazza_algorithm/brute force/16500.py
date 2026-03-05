# 백준 16500번
# 문자열 판별
# dfs

def is_string_buildable(text, arr):
    segments = [] 
    for i in range(len(arr)):
        target = arr[i]
        idx_list = string_matching(text, target)
        for j in range(len(idx_list)):
            segment = (idx_list[j], len(target)) # (segmentStart, offset)
            segments.append(segment)
    segments = sorted(segments,key=lambda x:x[0]) # segmentStart 기준 정렬
    
    visited = set()
    return dfs(0, len(text), segments, visited)
    

def dfs(start, end, segments, visited):
    # 성공 조건
    if start == end:
        return 1

    # 이미 실패한 위치면 중단
    if start in visited:
        return 0
    visited.add(start)

    # 이어질 수 있는 모든 segment 시도
    for seg_start, seg_len in segments:
        if seg_start == start:
            if dfs(start + seg_len, end, segments, visited):
                return 1
    return 0


def string_matching(text, target): 
    idx_list = []
    start = 0
    while(True):
        idx = text.find(target, start)
        if idx == -1:
            break
        else:
            idx_list.append(idx)
            start += 1
    return idx_list

S = input()
N = int(input())
A = []
for _ in range(N):
    A.append(input())
    
print(is_string_buildable(S, A))

"""
String 비교
A:
1xx0000 (0,3)
B:
01xxx00 (1,4)
0001xxx (3,4)
C:
0001xx0 (3,3)
D:
0000001 (6,1)

-> A,B 또는 A,C,D

반복:
    1. start == 1: True인 케이스 찾기
        else: 다른 거에서 반복
    2. start + len(case) == 1: True인 케이스 찾기
"""