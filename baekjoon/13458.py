N = int(input())
student = list(map(int, input().split()))

B, C = map(int, input().split())

supervisor = []

for i, A in enumerate(student):
  if A > B:
    if (A - B) % C == 0:
      supervisor.append(1 + ((A - B) // C))
    else:
      supervisor.append(1 + ((A - B) // C + 1))
  else:
    supervisor.append(1)


print(sum(supervisor))