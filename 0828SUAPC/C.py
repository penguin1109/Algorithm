import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())
remade = []
ans = 0
def find(board, length):
    global ans
    for i in range(N-length+1):
        for j in range(M-length+1):
        # 흰색으로 시작할 때, 검은색으로 시작할 때 각각에 대해 만들어지는지 확인
            valid_w, valid_b = True, True
            for k in range(i, i+length):
                for l in range(j, j+length):
                    if (k+l)%2 == 0:
                        if board[k][l] != 'W':
                            valid_w = False
                        if board[k][l] != 'B':
                            valid_b = False
                    else:
                        if board[k][l] != 'B':
                            valid_w = False
                        if board[k][l] != 'W':
                            valid_b = False
            if valid_w:ans+=1
            if valid_b:ans+=1

for i in range(2, min(N, M)+1):
    find(board, i)

print(ans+N*M)