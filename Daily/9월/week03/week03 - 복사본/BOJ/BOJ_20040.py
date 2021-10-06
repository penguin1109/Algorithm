# 사이클 게임
# 자료 구조, 분리 집합
import sys
from collections import deque
# 모든 경우를 전부 cycle을 탐색하도록 구현했더니 시간초과가 발생함
# 처음 자기 자신으로 돌아와야 한다는 점에서 일반적인 tree를 사용한 cycle과는 다른 disjoint set을 사용하는 문제
input = sys.stdin.readline

n, m = map(int, input().split())
data = [[]for _ in range(n)]
def check(data, start):
    # 지역 변수 n
    global n
    answer = False
    q = deque()
    q.append([str(start)])
    while q:
        node = q.popleft()
        for d in data[int(node[-1])]:
            if d == start and len(list(set(node))) >= 3:
                answer = True
                return answer
            if str(d) not in node:
                q.append(node + [str(d)])
    
    return answer
answer = 0
cycle = False
for _ in range(m):
    a, b = map(int, input().split())
    if cycle == True:
        continue
    # data에 연결돤 점 정보 입력
    data[a].append(b)
    data[b].append(a)

# cycle이 존재하는지 확인
for i in range(n):
    if check(data, i) == True:
        cycle = True
        answer = _+1
        break
print(answer)


