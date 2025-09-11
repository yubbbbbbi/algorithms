N, r, c = map(int, input().split())

def position(N, r, c, num):
  if N == 0:
    return num
  half = 2**(N - 1)
  quarter = 4**(N - 1)
  if r < half and c < half:
    return position(N - 1, r, c, num)
  if r < half and c >= half:
    return position(N - 1, r, c - half, num + quarter)
  if r >= half and c < half:
    return position(N - 1, r - half, c, num + 2 * quarter)
  if r >= half and c >= half:
    return position(N - 1, r - half, c - half, num + 3 * quarter)

print(position(N, r, c, 0))