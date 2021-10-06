#Kick Start Round E 2020
#1. Longest Arithemic
import sys
t = int(sys.stdin.readline())
def judge(diff):
    diff.append(-9999999999)
    length = -1
    curr = diff[0]
    temp = 2
    for k in range(1, n):
        if diff[k] == curr:
            temp += 1
        else:
            length = max(length, temp)
            temp = 2
            curr = diff[k]
    if length == -1:
        length = temp
    return length

        


def diff(num):
    diff = [0]*(n-1)
    for i in range(1,n):
        diff[i-1] = (num[i]-num[i-1])
    ans = judge(diff)
    return ans

for index in range(1,t+1):
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    res = diff(num)
    print('Case #%s: %s' %(str(index), str(res)))


#2. High Buildings
import sys
t = int(sys.stdin.readline())
def make(n,a,b,c):
    height = [n]*c
    s1 = a-c
    height = [n-1]*s1 + height
    s2 = b-c
    height = height + [n-1]*s2
    return height
def judge(height):
    res = True
    if len(height) > n:
        return False
    else:
        if len(height) < n:
            if a-c != 0:
                if height[0] > 1:
                    for i in range(a-c, a-c+(n-len(height))):
                        height.insert(i,height[0]-1)
                else:
                    return False
            elif b-c != 0:
                if height[-1] > 1:
                    for i in range(c,c+n-len(height)):
                        height.insert(i, height[-1]-1)
                else:
                    return False
            elif a-c == 0 and b-c == 0:
                if c == 1:
                    return False
                else:
                    for i in range(1, n-len(height)+1):
                        height.insert(i, height[0]-1)
    return res

for index in range(1, t+1):
    n,a,b,c = map(int, sys.stdin.readline().split())
    height = make(n,a,b,c)
    if judge(height):
        ans = ''
        for i in height:
            ans += str(i)+' '
        print('Case #%s: %s' %(str(index), str(ans)))
    else:
        print('Case #%s: %s' %(str(index), 'IMPOSSIBLE'))

#3. Toys
#첫번째 코드는 답은 맞게 나오나 메모리 초과가 발생한 코드이다.
#메모리 초과의 원인은 combinations로 만든 리스트였고, 원래 나는 길이 n의 1차원 리스트 때문이라고 생각했는데 알고 보니 그게 아니었다.
import sys
t = int(sys.stdin.readline())
from itertools import combinations
INF = float('inf')
def check(toy,i,k):
    global ans,idx
    time,forget = 0,0
    for p in k:
        time += toy[p][0]
        forget += toy[p][1]
    count = 0
    for p in k:
        e,r = toy[p][0], toy[p][1]
        if r <= time-e:count += 1
    if count == i:
        ans, idx = INF, n-i
        return
    else:
        end_time = [0]*n
        curr_time = 0
        while True:
            for _ in range(100000):
                for p in k:
                    e,r = toy[p][0], toy[p][1]
                    if end_time[p] == 0:
                        end_time[p] += curr_time + e
                        curr_time += e
                    else:
                        if curr_time-end_time[p] < r:
                            if ans < curr_time:
                                ans, idx = curr_time, n-i
                            return
                        else:
                            end_time[p] += time
                            curr_time += e


for index in range(1,t+1):
    n = int(sys.stdin.readline())
    toy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans,idx= 0,0
    def answer(n, toy):
        global ans, idx
        for i in range(n):
            file = list(combinations([int(l) for l in range(n)],n-i))
            for k in file:
                check(toy, n-i,k)
                if ans == INF:
                    return
    answer(n,toy)
    if ans == INF:
        print('Case #%s: %s %s' %(str(index), str(idx), 'INDEFIENTELY'))
    else:
        print('Case #%s: %s %s' %(str(index), str(idx), str(ans)))

#두번째 코드는 시간, 메모리 초과 모두 발생하지 않았는데 priority queue를 이용해서 해결했다.
from heapq import *
for _ in range(int(input())):
    n,t,time = int(input()), [], 0
    for i in range(n):
        play, rem = map(int,input().split())
        time += play
        t.append((play+rem, play))
    t2, curr, remove = sorted(t), time, 0
    while t2 and t2[-1][0] > curr:
        curr, remove = curr-t2.pop()[1], remove+1
    if t2:
        print('Case #'+str(_+1)+': '+str(remove)+' INDEFINITELY')
        continue  #이렇게 하면 제일 처음의 for문으로 이어감
    max_time, spent_time,min_del, delete, toy = time,time,0,0,[]
    for i in range(n):
        if t[i][0] <= time:
            spent_time += t[i][1]
            heappush(toy, (-t[i][0], t[i][1]))
        else:
            spent_time -= t[i][1]
            time -= t[i][1]
            delete += 1
            while toy and -toy[0][0] > time:
                temp = heappop(toy)[1]
                time -= temp
                spent_time -= temp*2
                delete += 1
        if spent_time > max_time:
            max_time = spent_time
            min_del = delete
    print('Case #'+str(_+1)+': '+str(min_del)+' '+str(max_time))
