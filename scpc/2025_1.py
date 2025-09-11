# scpc_1

T = int(input())
sold = [0] * T

for i in range(T):
  N = int(input())
  guest_money = list(map(int, input().split()))
  
  money_500 = 0
  money_1000 = 0
  money_5000 = 0

  
  for j in range(N):
    if guest_money[j] == 500:
      money_500 += 1
      sold[i] += 1
      
    elif guest_money[j] == 1000:
      if money_500 >= 1:
        money_500 -= 1
        money_1000 += 1 
        sold[i] += 1
        
    elif guest_money[j] == 5000:
      if money_500 >= 1 and money_1000 >= 4:
        money_500 -= 1
        money_1000 -= 4
        money_5000 += 1
        sold[i] += 1
        continue
      if money_500 >= 3 and money_1000 >= 3:
        money_500 -= 3
        money_1000 -= 3
        money_5000 += 1
        sold[i] += 1
        continue
      if money_500 >= 5 and money_1000 >= 2:
        money_500 -= 5
        money_1000 -= 2
        money_5000 += 1
        sold[i] += 1
        continue
      if money_500 >= 7 and money_1000 >= 1:
        money_500 -= 7
        money_1000 -= 1
        money_5000 += 1
        sold[i] += 1
        continue
      if money_500 >= 9:
        money_500 -= 9
        money_5000 += 1
        sold[i] += 1
        continue
        
for i in range(T):
  print(f"Case#{i + 1}")
  print(sold[i])