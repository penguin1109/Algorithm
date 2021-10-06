import sys
from collections import deque
# 처음에 그냥 브루트 포스로 모든 경우를 탐색하였고, 배열을 사용하였더니 시간 초과가 발생
# collections 모듈의 deque를 이용해서 
input = sys.stdin.readline
n, k = map(int, input().split())

# students 배열은 등수가 높은 사람부터 순서대로 이름의 길이가 담겨 있음
students = [] 
for i in range(n):
    name = str(input())
    students.append(len(name))

num = [0 for i in range(22)]

answer = 0

for i in range(3, 22):
    q = deque()
    for length in students:
        q.append(length)
        if len(q) > k+1:
            if q.popleft() == i:
                num[i] -= 1
        if length == i:
            if num[i] > 0:
                answer += num[i]
            num[i] += 1

print(answer)

