def solution(dirs):
    answer = 0
    x, y = 5, 5
    for i in range(len(dirs)):
        d = direction[dirs[i]]
        a, b = x + dx[d], y + dy[d]
        if (0<=a<=10 and 0<=b<=10):
            if (board[b][a][d] == 0 and board[y][x][abs(3-d)] == 0):
                board[b][a][d] = 1
                board[y][x][abs(3-d)] = 1
                answer += 1
            x,y=a,b

    return answer
board = [[[0,0,0,0]for _ in range(11)] for _ in range(11)]
direction = {'U' : 0, 'R':1,'L':2,'D':3}
dx, dy = [0, 1, -1, 0], [1, 0, 0 , -1]
dirs = ["ULURRDLLU","LULLLLLLU"]
for d in dirs:
    print(solution(d))