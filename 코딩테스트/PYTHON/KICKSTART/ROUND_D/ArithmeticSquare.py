import sys
input = sys.stdin.readline

def answer(x, y):
    print('Case #%s: %s'%(str(x), str(y)))

def check(matrix):
    dx, dy = [0,0,0,1],[0,1,2,2]
    di, dj = [2,2,2,1], [2,1,0,0]
    nums = dict()
    for k in range(4):
        i,j,x,y = di[k], dj[k], dx[k], dy[k]
        s = matrix[i][j] + matrix[x][y]
        if s//2 == s/2:
            if s in nums:
                nums[s] += 1
            else:nums[s] = 1
    result = 0
    for i, val in nums.items():
        if result < val:
            result = val
    dx, dy = [0,0,2,2], [0,2,2,0]
    di, dj = [0,2,2,0], [2,2,0,0]
    da, db = [0,1,2,1], [1,2,1,0]
    ans = 0
    for k in range(4):
        i,j,x,y = di[k], dj[k], dx[k], dy[k]
        a,b = da[k], db[k]
        if matrix[i][j] + matrix[x][y] == matrix[a][b]*2:
            ans += 1
    return ans+result

t = int(input())
for _ in range(t):
    matrix = []
    for j in range(3):
        insert = list(map(int, input().split()))
        if j == 1:
            temp = [insert[0], 0, insert[1]]
        else:
            temp = insert
        matrix.append(temp)
    
    ans = check(matrix)
    answer(_+1, ans)

    


