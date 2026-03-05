# 백준 4354번
# 문자열 제곱
# 문자열, KMP

def kmp_preprocessing(text):
    N = len(text)
    lps = [0] * N
    pre_ptr = 0
    for ptr in range(1, N):
        while pre_ptr > 0 and text[ptr] != text[pre_ptr]:
            pre_ptr = lps[pre_ptr-1]
        if text[ptr] == text[pre_ptr]:
            pre_ptr += 1
            lps[ptr] = pre_ptr
    return lps

def find_a_and_n(text):
    lps = kmp_preprocessing(text)
    L = len(text)
    k = L - lps[-1]
    
    if k > 0 and L % k == 0:
        return L // k
    else:
        return 1

text_list = []
while(True):
    text = input()
    if text == '.':
        break
    else:
        text_list.append(text)

for i in range(len(text_list)):
    print(find_a_and_n(text_list[i]))

'''
pspzpspz
00101234

abcd
0000

aaaa
0123
'''