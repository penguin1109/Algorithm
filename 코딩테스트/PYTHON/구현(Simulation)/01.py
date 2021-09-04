import sys
input = sys.stdin.readline

place = str(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x, y = 0, int(place[1])
for alp in alpha:
    if alp == place[0]:
        x = alpha.index(alp)

dx, dy = [2,2,-2,-2,1,1,-1,-1], [1,-1,1,-1,2,-2,2,-2]
for i in range(len(dx)):
    for j in range(len(dy)):
         

