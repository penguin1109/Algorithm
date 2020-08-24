#Kick Start Round C 2020
#Countdown
import sys
def check(n, k, file,idx):
    count = 0
    for i in range(len(idx)):
        a = 1
        for j in range(idx[i]+1, n):
            if file[j] == file[j-1]-1:
                a += 1
                if a == k:
                    count += 1
                    break
            else:
                break
    return count
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    file = list(map(int, sys.stdin.readline().split()))
    idx = []
    for j in range(n):
        if file[j] == k:
            idx.append(j)
    res = check(n, k, file,idx)
    print('Case #%s: %s'%(str(i + 1), str(res)))


#Stable Wall
t = int(input())
for case in range(t):
    r,c = map(int, input().split())
    past = ''
    dic = dict()
    for j in range(r):
        file = input()
        for k in file:
            if k not in dic:
                dic[k] = set()
        if len(past) != 0:
            for l in range(c):
                currentalph = past[l]
                pastalph = file[l]
                if currentalph != pastalph:
                    dic[currentalph].add(pastalph)
        past = file
    order = []
    bad = False
    for i in range(len(dic)):
        good = False
        for k in dic:
            if len(dic[k]) == 0:
                order.append(k)
                for j in dic:
                    if k in dic[j]:
                        dic[j].remove(k)
                dic[k].add('beasdera')
                good = True
                break
        if not good:
            bad = True
            break
    if bad:
        print('Case #'+str(case+1)+': '+str(-1))
    else:
        answer = ''
        for i in order:
            answer += str(i)
        print('Case #'+str(case+1)+': '+answer)
