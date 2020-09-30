### BOJ-17976-Thread Knots 
- 이분 탐색을 이용해서 해결하는 문제였다.
- 문제는 n개의 구간중에 각각 정수 좌표를 하나씩 선택하고 표시를 한 뒤에 각각의 표식중에 가장 가까운 거리로 가능한 값의 최댓값을 구하는 문제였다.
- 우선 최소이자 최대인 거리를 하나 정해서 정답으로 설정해 준 뒤에 해당 값을 정답으로 확정 지은 후 모든 경우를 그 거리로 계산해서 가능한지 아닌지의 여부를 따지는 것이었다.
- 일단 이분 탐색이다 보니 당연히 while문의 탈출 조건을 설정해 주어야 했고, ```while (left <= right)```로 설정해 주었다.
- 무조건 왼쪽 끝에 더 가까울 수록 더 긴 길이의 답을 얻을 수 있기 때문에 시작 표식은 항상 0으로 설정을 해 주었다.
  - 처음에는 left = mid, right = mid로 각각의 경우 갱신했더니 while 문을 ```while (left + 1 != right)```로 하고 초기 최대 길이에 1을 더해야만 시간 초과가 나지 않아서 그냥 left = mid-1, right = mid + 1로 갱신해 주었다.
```py3
import sys
n = int(input())
tile = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    tile.append((a,a+b))

tile = sorted(map(lambda x: (x[0], x[1]), tile))
ans = 0

def valid(length):
    left_end = 0
    for i in range(n):
        a,b = tile[i][0], tile[i][1]
        left_end = max(left_end, a)
        if left_end > b:return False
        left_end += length
    return True

left, right = 0, max(map(lambda x:x[1], tile))

while left <= right:
    mid = (left + right) //2
    if valid(mid):
        ans = mid
        left = mid+1
    else:
        right = mid-1


print(ans)
```
