# scpc_2

T = int(input())
distance = [0] * T

for i in range(T):
  N, L = map(int, input().split())
  bomb = list(map(int, input().split()))

  route = [-1] * N
  
  for j in range(N):
    k = bomb[j]
    
    if j == 0: # 처음 폭탄
      route[j] = 0
      continue
    
    if route[j] != -1:
      continue
      
    if j == N - 1: # 마지막 폭탄
      if k <= L // 2:
        route[j] = 0
      else:
        route[j] = 1
      break
      
    l = bomb[j + 1]
    if k <= L // 2 and l <= L // 2: # case 1: A -> A
      route[j] = 0
    if k <= L // 2 and l > L // 2: # case 2: A -> B
      if k < L - l:
        route[j] = 0
        route[j + 1] = 0 # B는 0에서 시작
      else:
        route[j] = 1
    if k > L // 2 and l > L // 2: # case 3: B -> B
      route[j] = 1
              
  for j in range(N):
    if bomb[j] <= L // 2:
      if route[j] == 0:
        distance[i] += 2 * bomb[j]
      else:
        distance[i] += L
    if bomb[j] > L // 2:
      if route[j] == 0:
        distance[i] += L
      else:
        distance[i] += 2 * (L - bomb[j])


for i in range(T):
  print(f"Case#{i + 1}")
  print(distance[i])

