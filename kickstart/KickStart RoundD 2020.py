#Kick Start Round D 2020
#Record Breaker
import sys
t = int(sys.stdin.readline())
def check(file):
    ans, big = set(), -99
    if n == 1:
        return 1
    for i in range(n):
        if i == 0:
            if file[i] > file[i+1]:
                ans.add(i)
        elif i == n-1:
            if file[i] > big:
                ans.add(i)
        else:
            if file[i] > file[i+1] and file[i] > big:
                ans.add(i)
        big = max(big, file[i])
    return len(ans)
for i in range(t):
    n = int(sys.stdin.readline())
    file = list(map(int, sys.stdin.readline().split()))
    res = check(file)
    print('Case #%s: %s' %(str(i+1), str(res)))


#Alien Piano
import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    file = list(map(int, sys.stdin.readline().split()))
    up, down = 0,0
    res = 0
    for j in range(1,n):
        if file[j] < file[j-1]:
            down += 1
            up = 0
        elif file[j] > file[j-1]:
            up += 1
            down = 0
        if up > 3 or down > 3:
            res += 1
            up, down = 0,0
    print('Case #%s: %s' %(str(i+1), str(res)))


