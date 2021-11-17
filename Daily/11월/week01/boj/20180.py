# 백준 20180 - Two Buildings
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

answer = -1
L, R = [],[] #왼쪽 아래의 점의 집합 / 오른쪽 아래의 점의 집합
for i in range(n):
    L.append((i, -heights[i]))
    R.append((i, heights[i]))
S = [-1 for _ in range(n)] # Li와 연결해서 직사각형이 되는 Uk중에서 넓이가 최대인 Si

def solve(l, r, optl, optr):
    global answer,S
    """
    optl (int) : L배열의 l번째 점을 한 꼭지점으로 가질때에 최대 넓이를 만드는 R배열에서의 좌표
    optr (int) :
    """
    if (l > r):return
    mid = (l+r)//2
    opt = optl
    ans = S[mid]
    for i in range(optl, optr+1, 1):
        dt = R[i][0] - L[mid][0]
        dp = R[i][1] - L[mid][1]
        if (dt >= 0 or dp >= 0):
            val = dt*dp
            if (ans <= val):
                ans = val
                S[mid] = ans
                opt = i
    solve(l, mid-1, optl, opt)
    solve(mid+1, r, opt, optr)

    answer = max(answer, ans)


solve(0, n-1, 0, n-1)
print(answer)