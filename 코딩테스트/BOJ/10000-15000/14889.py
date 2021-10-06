# 스타트와 링크
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소화 하고자 한다.

import sys, math
# 사용되는 알고리즘 : 백트래킹은 이미 지나쳐 온 곳을 다시 돌아가서 다른 가능성을 시도해 보는 것 (dfs로 가능)
# 브루트 포스는 말 그대로 모든 경우의 수를 대입해 보는 방법
# dfs는 여러 지점을 한 단계씩 거치면서 탐색하고 스택의 개념으로 이전 단계로 가서 반복해 보는 것이다.
"""
# j라는 index값을 보내고 gropu_a, group_b를 만들어서 재귀적으로 구현을 했음
# 그러나 최적화를 했다고 생각했음에도 시간 초과가 발생

input = sys.stdin.readline

n = int(input())

info = [list(map(int, input().split(' '))) for _ in range(n)]
sums= 0
for i in range(n):
    sums += sum(info[i])
answer = math.inf

def calc(group):
    s = 0
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            a, b = int(group[i]), int(group[j])
            s += info[a][b] + info[b][a]
    return s

def add_score(a, b):
    return info[a][b] + info[b][a]
mem = ''.join(str(x) for x in range(n))
def solve(group_a, group_b, i):
    global answer
    if len(group_a) == n//2:
        answer = min(answer, abs(calc(group_a)-calc(group_b)))
        return
    elif len(group_a) < n//2:
        for j in range(i+1, n):
            solve(group_a + str(j), group_b, j)
            solve(group_a, group_b + str(j), j)


solve('0', '', 0)
print(answer)

"""

import sys, math
from itertools import combinations

input = sys.stdin.readline

n = int(input())

info = [list(map(int, input().split(' '))) for _ in range(n)]
# i, j를 new의 k반째 요소라고 할 때에 k와 같은 팀이 되었을 떄의 능력치의 가로 방향, 세로 방향의 합을 의미
new = [sum(i)+sum(j) for i, j in zip(info, zip(*info))]

all = sum(new)//2

answer = math.inf

# new 가 배열이기 때문에 new[:-1]을 해서 한번 풀어준다.
for i in combinations(new[:-1], n//2):
    # 전체 사람의 절반만큼 한 팀을 이루기 떄문에 그 만큼 조합을 구해 준다.
    answer = min(answer, abs(all - sum(i)))

print(answer)
