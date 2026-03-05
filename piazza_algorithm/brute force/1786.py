# 백준 1786번
# 찾기
# 문자열, KMP

def kmp_preprocessing(text):
    N = len(text)
    lps = [0] * N
    
    pre_ptr = 0
    for ptr in range(1, N):
        # mismatch 발생
        while (pre_ptr > 0 and text[ptr] != text[pre_ptr]): # prefix 포인터 재설정
            pre_ptr = lps[pre_ptr-1] 
            # prefix 포인터가 0이 되는 경우 break
            # match가 발생하는 경우 break
        
        # match 발생
        if text[pre_ptr] == text[ptr]:
            pre_ptr += 1
            lps[ptr] = pre_ptr
    return lps
                    
def kmp(text, pattern):
    lps = kmp_preprocessing(pattern)
    res = []
    
    pre_ptr = 0
    N, M = len(text), len(pattern)
    for ptr in range(N): 
        # mismatch 발생 
        while (pre_ptr > 0 and text[ptr] != pattern[pre_ptr]): # 포인터 재설정
                pre_ptr = lps[pre_ptr-1] 
        
        # match 발생 
        if pattern[pre_ptr] == text[ptr]:
            if pre_ptr == M-1: # 패턴 전체가 매칭된 경우
                res.append(ptr-M+2)
                pre_ptr = lps[pre_ptr]
            else:
                pre_ptr += 1
    return res

T = input()
P = input()

result = kmp(T,P)
print(len(result))
for i in range(len(result)):
    print(result[i])
    
'''
01234567890123456789012
ABC ABCDAB ABCDABCDABDE
ABCDABD


0123 4567 - 현재 pre_ptr = 3 ptr = 7
AAAC AAAA - 비교 pre_ptr = 2 ptr = 7
0120 1233

ADAC ADAD
0010 1232

012345
ABABAC - 현재 pre_ptr = 3 ptr = 5
001230 - 비교 pre_ptr = 1 ptr = 5

ABCD ABF ABCD
0000 120 1234

ABC ABCDAB ABCDABCDABDE

ABCD ABD
0000 120

2초: 10^16
n, m = 10^6
패턴이 나타나기 전: 그대로 이어서
패턴이 나타난 후: 패턴부터 이어서

출력: n번 + index
'''