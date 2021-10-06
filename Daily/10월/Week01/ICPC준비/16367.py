# 16367 - TV Show Game
import sys, itertools
input = sys.stdin.readline
# k개의 불빛 n명의 사람
k, n = map(int, input().split())
pr = [[0 for _ in range(k)]for _ in range(n)]
def change(color):
    if (color == 'B'):
        return 1
    else:
        return 2

def bfs(order):
    answer = 0
    count = [0 for _ in range(n)]
    for i in range(k):
        curr = order[i]
        for j in range(n):
            if int(curr) == pr[j][i]:
                count[j] += 1
    for i in range(n):
        if count[i] >= 2:
            answer += 1
    if answer == n:
        return True
    else:return False

def make(order):
    if len(order) == k:
        orders.append(order)
        return
    else:
        make(order + str(1))
        make(order + str(2))
        
orders = []
for _ in range(n):
    predict = list(map(str, input().split()))
    for i in range(0, len(predict), 2):
        lamp, color = int(predict[i]), change(predict[i+1])
        pr[_][lamp-1] = color

make('')
valid = False
for o in orders:
    if bfs(o):
        valid = True
        result = ''
        for ch in o:
            if ch == '1':
                result += 'R'
            else:
                result += 'B'
        print(result)
        break
if not valid:
    print(-1)






