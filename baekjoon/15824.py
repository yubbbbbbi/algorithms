"""
from itertools import combinations
spicyCombi = [] 
for i in range(2, N+1):
  spicyCombi.append(list(combinations(spicyList, i)))

res = []
for spicyByCombi in spicyCombi:
  for spicys in spicyByCombi:
    res.append(max(spicys) - min(spicys))

result = sum(res) % 1000000007
print(result)
"""

MOD = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))
A.sort()

pow = [1] * N 

for i in range(1, N):
  pow[i] = (pow[i - 1] * 2) % MOD

res = []
for i, spicy in enumerate(A):
 res.append((spicy * (pow[i] - pow[N - 1 - i])) % MOD)

print(sum(res) % MOD)