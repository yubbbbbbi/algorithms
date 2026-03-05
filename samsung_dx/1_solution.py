# 26 동계 대학생 알고리즘 특강 사전 문제
# 타일 매칭

from typing import List

EMPTY = 0
H = 8
W = 8

board = [[0]*W for _ in range(H)]
reserve = []
reserve_ptr = [0]*W


def score_by_len(k):
    if k == 3:
        return 1
    if k == 4:
        return 4
    return 9


def init(N, mTiles):
    global board, reserve, reserve_ptr
    reserve = mTiles
    reserve_ptr = [0]*W
    board = [[EMPTY]*W for _ in range(H)]
    apply_gravity()


def apply_gravity():
    for x in range(W):
        fill_y = 0
        for y in range(H):
            if board[y][x] != EMPTY:
                board[fill_y][x] = board[y][x]
                fill_y += 1
        while fill_y < H:
            board[fill_y][x] = reserve[reserve_ptr[x]][x]
            reserve_ptr[x] += 1
            fill_y += 1


def clear_all_matches():
    mark = [[False]*W for _ in range(H)]
    score = 0

    # 가로
    for y in range(H):
        x = 0
        while x < W:
            if board[y][x] == EMPTY:
                x += 1
                continue
            nx = x
            while nx < W and board[y][nx] == board[y][x]:
                nx += 1
            length = nx - x
            if length >= 3:
                for i in range(x, nx):
                    mark[y][i] = True
                score += score_by_len(length)
            x = nx

    # 세로
    for x in range(W):
        y = 0
        while y < H:
            if board[y][x] == EMPTY:
                y += 1
                continue
            ny = y
            while ny < H and board[ny][x] == board[y][x]:
                ny += 1
            length = ny - y
            if length >= 3:
                for i in range(y, ny):
                    mark[i][x] = True
                score += score_by_len(length)
            y = ny

    if score == 0:
        return 0

    for y in range(H):
        for x in range(W):
            if mark[y][x]:
                board[y][x] = EMPTY

    return score


def prepare():
    while True:
        # 1-a 빈칸 채우기
        if any(board[y][x] == EMPTY for y in range(H) for x in range(W)):
            apply_gravity()
            continue

        # 1-b 자동 삭제
        if clear_all_matches() > 0:
            apply_gravity()
            continue

        # 1-c 교환 가능 여부
        possible = False
        for y in range(H):
            for x in range(W):
                if x+1 < W and immediate_score(y,x,y,x+1) > 0:
                    possible = True
                if y+1 < H and immediate_score(y,x,y+1,x) > 0:
                    possible = True
        if not possible:
            for y in range(H):
                for x in range(W):
                    board[y][x] = EMPTY
            apply_gravity()
            continue

        break


def line_score(y, x, dy, dx):
    v = board[y][x]
    cnt = 1
    ny, nx = y+dy, x+dx
    while 0 <= ny < H and 0 <= nx < W and board[ny][nx] == v:
        cnt += 1
        ny += dy
        nx += dx
    ny, nx = y-dy, x-dx
    while 0 <= ny < H and 0 <= nx < W and board[ny][nx] == v:
        cnt += 1
        ny -= dy
        nx -= dx
    if cnt >= 3:
        return score_by_len(cnt)
    return 0


def immediate_score(y1,x1,y2,x2):
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]

    s = 0
    for y,x in ((y1,x1),(y2,x2)):
        s += line_score(y,x,1,0)
        s += line_score(y,x,0,1)

    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]
    return s


def takeTurn() -> List[int]:
    prepare()

    best = None
    for y in range(H):
        for x in range(W):
            if x+1 < W:
                s = immediate_score(y,x,y,x+1)
                if s > 0:
                    cand = (-s, y, x, 0)
                    if best is None or cand < best:
                        best = cand
            if y+1 < H:
                s = immediate_score(y,x,y+1,x)
                if s > 0:
                    cand = (-s, y, x, 1)
                    if best is None or cand < best:
                        best = cand

    if best is None:
        return [0,0,0,0,0]

    _, y, x, d = best
    ny, nx = (y, x+1) if d == 0 else (y+1, x)
    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

    total = 0
    while True:
        s = clear_all_matches()
        if s == 0:
            break
        total += s
        apply_gravity()

    return [total, y, x, ny, nx]
