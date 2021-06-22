import sys
input = sys.stdin.readline

# 0과 1로만 이루어진 문자열
# 문자열을 모두 같은 수로 만들기 위한 최소의 뒤집는 횟수

q = list(map(int, input().strip()))
zeros, ones = 0,0

while q:
    curr = q.pop()
    if curr == 0:
        zeros += 1
    else:
        ones += 1
    while (q and q[-1] == curr):
        q.pop()
print(min(zeros, ones))