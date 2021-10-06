# Sol02 -> 이분 탐색 -> pypy3으로 제출해야만 시간 초과가 발생하지 않는다.
# 해결하고 보니 전형적인 이분탐색 문제였다.
# 만약에 valid하다면 더 긴 길이도 가능할 수도 있는 것이므려 left = mid + 1을 해 줄 조건이 성립
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse = True)

answer = 0 
left, right = 1, max(arr)

def check(val):
    count = 0
    for i in range(N):
        count += arr[i]//val
    if count >= M:
        return True
    else:
        return False
answer = 0
while (left <= right):
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)

# 13301 - 타일 장식물
# 간단한 수학문제 -> 피보나치 수열을 찾는 등의 규칙성을 확인하면 되는 문제
import sys
input = sys.stdin.readline

N = int(input())
answer = 4
if N == 1:answer = 4
else:
    a, b = 1, 2
    for i in range(1, N):
        answer += 2*a
        a,b = a+b, b
print(answer)

# 6996 - 애너그램
def anagram(a, b):
    dicta = {}
    a, b = a.strip(), b.strip()
    if len(a) != len(b):
        return False
    else:
        for i in list(set(a)):
            dicta[i] = 0
        for i in a:
            dicta[i] += 1
        for i in b:
            if i in dicta:
                if dicta[i] > 0:
                    dicta[i] -= 1
                else:
                    return False
            else:
                return False
    return True


        


T = int(input())
for i in range(T):
    A, B = map(str, input().split())
    if anagram(A, B):
        print('{} & {} are anagrams.'.format(A, B))
    else:
        print('{} & {} are NOT anagrams.'.format(A, B))

# 2668 - 숫자 고르기
# dfs와 그래프의 cycle을 이루는 것을 찾는 것이다.

# Sol01 -> dfs 사용
def dfs(a,start): # start변수는 계속 유지
    visited[a] = 1
    node = nums[a]
    if visited[node] == 0: # 방문한적이 없다면 dfs 함수 재귀 적용
        dfs(node, start)
    elif visited[node] == 1 and node == start: # 방문 한적이 있으면서 cycle을 이룬다면 해당 노드를 답이 되도록 한다.
        answer.append(node)

T = int(input())
nums = [int(input()) for _ in range(T)]
nums.insert(0,0)
answer = []
for i in range(1, T+1):
    visited = [0]*(T+1)
    dfs(i, i)

print(len(answer))
answer = sorted(answer)
for i in answer:
    print(i)

# Sol02 -> set사용
import sys
N = int(input())
nums = [int(input()) for i in range(N)]
nums.insert(0,0) # list의 앞에 0을 삽입 -> index편하게 다루기 위해

sets = set() # python의 set을 이용하면 중복 제거 가능

for i in range(1, N+1):
    stack = [(i, [i])]
    while stack:
        node, nodes = stack.pop()
        if nums[i] == node: # cycle을 이률 때
            sets.update(set(nodes))
            break
        for j in range(1, N+1):
            if nums[j] == node:
                stack.append((j, nodes+[j]))
sets = sorted(list(sets))
print(len(sets))
for i in sets:
    print(i)