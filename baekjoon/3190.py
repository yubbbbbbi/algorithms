from collections import deque

n = int(input())
grid = [[0] * n for _ in range(n)] # 맵 n*n

apple = [] 
m = int(input())
for _ in range(m):
  x, y = map(int, input().split())
  grid[x-1][y-1] = 1 # 사과 위치 정보 

queue = deque() # 이동 및 회전 정보 (step, dir)
k = int(input())
for _ in range(k):
  time, d = input().split()
  queue.append((int(time), d))


# dir: 0=오른쪽, 1=아래, 2=왼쪽, 3=위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def game():
  dir = 0
  time = 0
  snake = deque()
  snake.append((0,0))
  grid[0][0] = 2

  while True:
    time += 1
    head_x, head_y = snake[-1]
    nx = head_x + dx[dir]
    ny = head_y + dy[dir]
    if (nx < 0 or nx >= n or ny < 0 or ny >= n) or grid[nx][ny] == 2:
      return time
    if grid[nx][ny] == 1: # 사과 유
      grid[nx][ny] = 2
      snake.append((nx, ny))
    else: # 사과 무
      grid[nx][ny] = 2
      snake.append((nx, ny))
      tx, ty = snake.popleft()
      grid[tx][ty] = 0

    if queue and queue[0][0] == time: # 방향 전환
      _, d = queue.popleft()
      if d == 'L': 
        dir = (dir - 1) % 4
      else:
        dir = (dir + 1) % 4
  
print(game())