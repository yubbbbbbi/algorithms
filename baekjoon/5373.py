#실패!!!!!!!!!!!!!!!!
def inint_cube():
  return  {
    'U' : [['w'] * 3 for _ in range(3)],
    'D' : [['y'] * 3 for _ in range(3)],
    'F' : [['r'] * 3 for _ in range(3)],
    'B' : [['o'] * 3 for _ in range(3)],
    'L' : [['g'] * 3 for _ in range(3)],
    'R' : [['b'] * 3 for _ in range(3)],
  }

# 시계방향 기준 인접 큐브
adj = { 
  'U' : [('B', 0, 'r'), ('R', 0, 'r'), ('F', 0, 'r'), ('L', 0, 'r')],
  'D' : [('F', 2, 'r'), ('R', 2, 'r'), ('B', 2, 'r'), ('L', 2, 'r')],
  'F' : [('U', 2, 'r'), ('R', 0, 'c'), ('D', 0, 'r'), ('L', 2, 'c')],
  'B' : [('U', 0, 'r'), ('L', 0, 'c'), ('D', 2, 'r'), ('R', 2, 'c')],
  'L' : [('U', 0, 'c'), ('F', 0, 'c'), ('D', 0, 'c'), ('B', 2, 'c')],
  'R' : [('U', 2, 'c'), ('B', 0, 'c'), ('D', 2, 'c'), ('F', 2, 'c')]
}


def RotateSide(face, sign, cube): # 옆면 회전
  neighbors = adj[face]
  
  rotated = []
  for side, index, matrix in neighbors: # 돌려지는 옆면 리스트에 삽입
    if matrix == 'r':
      rotated.append(cube[side][index][:])
    elif matrix == 'c':
      rotated.append([cube[side][row][index] for row in range(3)])

  if sign == '+':
    rotated = rotated[-1:] + rotated[:-1]
    
  else:
    rotated = rotated[1:] + rotated[:1]

  for i, (side, index, matrix) in enumerate(neighbors):
    if matrix == 'r':
      cube[side][index][:] = rotated[i]
      
    elif matrix == 'c':
      for row in range(3):
        cube[side][row][index] = rotated[i][row]
        

def RotateFace(face, sign, cube): # 바라보는 면 회전
  temp = [[0] * 3 for _ in range(3)]
  for i in range(3):
    for j in range(3):
      temp[i][j] = cube[face][i][j]
  if sign == '+':
    for col in range(2, -1, -1):
      for row in range(3):
        cube[face][row][col] = temp[2 - col][row]
  elif sign == '-':
    for col in range(3):
      for row in range(2, -1, -1):
        cube[face][row][col] = temp[col][2 - row]


def PrintUpperSide(cube):
  for i in range(3):
    for j in range(3):
      print(cube['U'][i][j], end="")
    print()


n = int(input())
cubing = []

for _ in range(n):
  _ = int(input())
  cubing.append(input().split())  
  
for i in range(len(cubing)): # 1회
  cube = inint_cube()
  for j in range(len(cubing[i])): # 하나씩 확인
    face = cubing[i][j][0]
    sign = cubing[i][j][1]
    neighbors = adj[face] 
    RotateSide(face, sign, cube)
    RotateFace(face, sign, cube)
  PrintUpperSide(cube)