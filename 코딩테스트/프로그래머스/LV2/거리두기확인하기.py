def solution(places):
    answer = []

    def check(a, b, places):
        dx, dy = [1,-1,0,0,1,-1,1,-1], [0,0,1,-1,1,-1,-1,1]
        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < 5 and 0 <= y < 5:
                if places[x][y] == 'P':
                    return False
                if places[x][y] == 'O':
                    x, y = a + dx[i]*2, b + dy[i]*2
                    if 0 <= x < 5 and 0 <= y < 5:
                        if places[x][y] == 'P':
                            return False
        for i in range(4, len(dx)):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < 5 and 0 <= y < 5:
                if places[x][y] == 'P':
                    if places[x][b] != 'X' or places[a][y] != 'X':
                        return False
        return True

    for place in places:
        new = [list(map(str, p.strip())) for p in place]
        safe = True
        for i in range(5):
            if safe == False:
                break
            for j in range(5):
                if new[i][j] == 'P':
                    if check(i,j,new) == False:
                        safe = False
                        break
        if safe == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer


    

