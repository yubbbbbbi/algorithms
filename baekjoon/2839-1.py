# 그리디 알고리즘
import time
start_time = time.time()

n = int(input())

result  = -1
reminder = n % 5
res1 = n // 5

while(True):
  if(reminder % 3 == 0):
    res2 = reminder // 3
    result = res1 + res2
    break
  elif(res1 == 0):
    break
  else:
    res1 -= 1
    reminder = (n - 5*res1)

print(result)

end_time = time.time()
print("time: ", end_time - start_time)