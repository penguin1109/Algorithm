#Kick Start Round B 2020
#Bike Tour
def check(height):
    global ans
    for i in range(1, len(height)-1):
        if height[i] > height[i-1] and height[i] > height[i+1]:
            ans += 1
t = int(input())
for i in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    ans = 0
    check(height)
    print('Case #%s: %s' %(str(i+1), str(ans)))



#Bus Routes
t = int(input())
for case in range(t):
    n,d = map(int, input().split())
    file = list(map(int, input().split()))
    left, right = 0,d
    m = 0
    while left < right:
        m = (left+right+1)//2
        day = m
        for i in range(n):
            a = file[i]
            if day % a > 0:
                day += a-(day%a)
        if day <= d:
            left, right = m, right
        else:
            left, right = left, m-1
    print('Case #%s: %s' %(str(case+1), str(left)))
