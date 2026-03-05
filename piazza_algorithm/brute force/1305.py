# 백준 1305번
# 광고
# 문자열, KMP

def kmp_preprocessing(text):
    N = len(text)
    lps = [0] * N
    
    pre_ptr = 0
    for ptr in range(1, N):
        while (pre_ptr > 0 and text[ptr] != text[pre_ptr]):
            pre_ptr = lps[pre_ptr-1]
        
        if text[ptr] == text[pre_ptr]:
            pre_ptr += 1
            lps[ptr] = pre_ptr
    return lps

_ = int(input())
text = input()
lps = kmp_preprocessing(text)
print(len(text) - lps[-1])

'''
abcdef
000000

ababab
001234

aabaaa
010122

aaaaaa
012345

abaaab
001112
'''