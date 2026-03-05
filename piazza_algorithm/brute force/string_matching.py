def string_matching(text, target):
    idx_list = []
    start = 0
    while(True):
        idx = text.find(target, start)
        if idx == -1:
            break
        else:
            idx_list.append(idx)
            start = idx + 1
    return idx_list, len(idx_list)

f = open("brute force/TheLittlePrince.txt", "r", encoding="utf-8")
text = f.read()
idx_list, count = string_matching(text, '어린 왕자')

print(f"총 {count}번 등장")
print("등장 인덱스:", end=" ")
for i in range(len(idx_list)):
    print(idx_list[i], end=" ")
f.close()