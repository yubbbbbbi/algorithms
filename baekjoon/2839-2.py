# 동적 계획법
import time
start_time = time.time()

n = int(input())

INF = 100000

dp = [INF] * 5050
dp[0] = 0
kilogram = [3, 5]

for i in range(len(kilogram)):
  for j in range(n + 1):
    if dp[j] != INF:
      dp[j + kilogram[i]] = min(dp[j + kilogram[i]], dp[j] + 1)

if dp[n] == INF:
  print(-1)
else:
  print(dp[n])


end_time = time.time()
print("time: ", end_time - start_time)