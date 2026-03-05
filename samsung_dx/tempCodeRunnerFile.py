import sys
from solution import init, takeTurn

CMD_INIT = 100
CMD_TAKETURN = 200

def run():
    okay = False
    Q = int(input())

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mTiles = [[0] * 8 for _ in range(N)]
            for y in range(N):
                input_iter = iter(input().split())
                for x in range(8):
                    mTiles[y][x] = int(next(input_iter))

            init(N, mTiles)
            okay = True
        elif cmd == CMD_TAKETURN:
            user_ans = takeTurn()
            for i in range(5):
                correct_ans = int(next(input_iter))
                if user_ans[i] != correct_ans:
                    okay = False
        else:
            okay = False
    return okay


#sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score), flush = True)