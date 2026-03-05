# 백준 1701번
# Cubeditor
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
    return max(lps)

text = input()
result = []

for i in range(len(text)):
    result.append(kmp_preprocessing(text[i:]))
print(max(result)) 


'''
abcdbcdbcd
 000000000
  00123456
   0012345
    001201
     ...
       001
        00
         0
'''