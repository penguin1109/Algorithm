def check(matrix):
    dx, dy = [0, 0, 0, 1], [0, 1, 2, 2]
    nums = dict()
    for k in range(4):
        i, j = dx[k], dy[k]
        x, y = abs(2-i), abs(2-j)
        s = matrix[i][j] + matrix[x][y]
        if s in nums:
            nums[s] += 1
        else:nums[s] = 1
    
    dx, dy = [0,0,0,2], [0,0,2,0]
    for k in range(4):
        i, j = dx[k], dy[k]
        x, y = abs(2-i), j
        s = matrix[i][j] + matrix[x][y]
        if s in nums:
            nums[s] += 1
        else:nums[s] = 1
        x, y =  i, abs(2-j)
        s = matrix[i][j] + matrix[x][y]
        if s in nums:
            nums[s] += 1
        else:nums[s] = 1
    ans = 0
    for i, val in nums.items():
        if ans < val:
            ans = val
    return ans 

    

