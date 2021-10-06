import sys
input = sys.stdin.readline

# 1. j개의 추가 조각들을 만들수 있는 지점의 개수를 a(j)라고 하자
# 2. 결과값에 j * a(j)를 더해준다면, c = min(c, a(j))로 바꾸어 주면서 c가 0이 될때까지 반복
# 3. Greedy Algorithm을 사용한 것



def answer(x, y):
    print('Case #%s: %s'%(str(x), str(y)))
# 특정 지점을 설정해서 모든 interval에 대해서 잘라주었을 떄의 조각의 모든 개수를 구해야 하며
# 이때에 조각의 개수가 최대가 되도록 하는 것이 목적
# 수가 크면 시간 초과 문제를 피하기 어려울 것

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    start, end = dict(), dict()
    answer = 0
    for _ in range(n):
        nums = []
        cut = 0
        a, b = map(int, input().split())
        nums.append((a, b))
        if a+1 in start:start[a+1] += 1
        else:start[a+1] = 1
        if b-1 in start:start[b-1] += 1
        else:start[b-1] = 1

        start, end = sorted(start.items(), reverse = True), sorted(end.items(), reverse = True)
        for i, j in enumerate(zip(start.keys(), end.keys())):
            

        

    
    
