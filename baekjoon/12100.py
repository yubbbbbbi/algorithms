from collections import deque
from copy import deepcopy

n = int(input())

board = []

for i in range(n):
  board.append(list(map(int, input().split())))
  
# 위로 아래로 왼쪽으로 오른쪽으로 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
depth = 0

def bfs(board):
  queue = deque()
  queue.append((deepcopy(board), 0))
  max_num = 0
  while queue:
    board, depth = queue.popleft()
    max_num = max(max_num, MaxBlockNum(board))
    if depth == 5:
      continue
    for dir in range(4):
      next_board = deepcopy(board)
      merged = [[0] * n for _ in range(n)]
      if dir == 0: # 위로 이동
        for y in range(n):
          for x in range(n):
            if next_board[x][y] == 0:
              continue
            move(next_board, merged, x, y, dx[dir], dy[dir])   
        queue.append((next_board, depth + 1))
        
      elif dir == 1: # 아래로 이동
        for y in range(n):
          for x in range(n - 1, -1, -1):
            if next_board[x][y] == 0:
              continue
            move(next_board, merged, x, y, dx[dir], dy[dir])   
        queue.append((next_board, depth + 1))

      elif dir == 2: # 왼쪽으로 이동
        for x in range(n):
          for y in range(n):
            if next_board[x][y] == 0:
              continue
            move(next_board, merged, x, y, dx[dir], dy[dir])   
        queue.append((next_board, depth + 1))
        
      elif dir == 3: # 오른쪽으로 이동
        for x in range(n):
          for y in range(n - 1, -1, -1):
            if next_board[x][y] == 0:
              continue
            move(next_board, merged, x, y, dx[dir], dy[dir])   
        queue.append((next_board, depth + 1))
  return max_num


def move(board, merged, x, y, dx, dy):
  block_num = board[x][y] 
  while True: # 블록 이동
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      break
    if board[nx][ny] != 0:
      if board[nx][ny] == block_num : # 같은 블록인 경우
        if merged[nx][ny] == 1: # 이미 합쳐진 블록
          break
        else: # 합치기
          board[x][y] = 0
          merged[nx][ny] = 1
          board[nx][ny] = 2 * block_num
          break 
      else: # 다른 블록인 경우
         break
    elif board[nx][ny] == 0: # 이동
      board[x][y] = 0
      x = nx
      y = ny
      board[nx][ny] = block_num

def MaxBlockNum(board):
  max_block_num = 0
  for i in range(n):
    for j in range(n):
      max_block_num = max(max_block_num, board[i][j])
  return max_block_num


print(bfs(board))