from collections import deque

n, m = map(int, input().split())

symbol_map = {
  '#' : 0,
  '.' : 1,
  'R' : 1,
  'B' : 1,
  'O' : -1
}

board = []

for i in range(n):
  row = input()
  row_nums = []
  for j, value in enumerate(row):
    row_nums.append(symbol_map[value])
    if value == 'R':
      rx, ry = (i, j)
    elif value == 'B':
      bx, by = (i, j)
  board.append(row_nums)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
depth = 0

def move(x, y, dx, dy):
  cnt = 0
  while True:
    if board[x][y] == -1:
      break
    if board[x + dx][y + dy] == 0:
      break
    x += dx
    y += dy
    cnt += 1
  return x, y, cnt
  

def bfs(rx, ry, bx, by):
  queue = deque()
  queue.append((rx, ry, bx, by, 0))
  visited = set()
  while queue:
    rx, ry, bx, by, depth = queue.popleft()
    
    if depth >= 10:
      return -1
      
    for i in range(4):
      nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) # 한 줄씩 이동
      nbx, nby, bcnt = move(bx, by, dx[i], dy[i]) # 한 줄씩 이동

      if board[nbx][nby] == -1: # B가 구멍에 통과
        continue
      if board[nrx][nry] == -1: # R이 구멍에 통과
        return depth + 1
        
      if (nrx, nry) == (nbx, nby): # 겹치는 경우 
        if rcnt > bcnt:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]
      
      if (nrx, nry, nbx, nby) not in visited: # 새로운 위치 큐에 추가
        queue.append((nrx, nry, nbx, nby, depth + 1))
        visited.add((nrx, nry, nbx, nby))
  return -1

print(bfs(rx, ry, bx, by))