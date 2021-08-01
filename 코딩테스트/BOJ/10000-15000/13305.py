# 그리디 알고리즘 (41점 - 부분 성공 -> n의 개수가 1000을 넘어가니 실패한 듯 하다)
# 자료구조로 list만 사용하다가 heapq로 바꾸어서 우선순위 큐를 이용했음에도 계속 시간 초과가 발생

# 처음에는 문제를 풀때에 해당 위치에서 남은 길이를 length라는 배열을 새롭게 만들어서 다시 저장
# 이후에 length 배열의 값과 cost배열의 값을 cost를 오름차순 기준으로 정렬해서 저장한 data라는 배열을 또 만들었음
# 그리고 data에서 작은 cost순서대로 남은 길이를 모두 이동할 수 있도록 기름을 사고 나머지 cost들에서는 이동 길이를 지웠는데
# data배열을 만들고 정렬하는 과정에서 heapq를 사용하더라도 시간 초과가 나기 때문에 
# 그냥 money변수를 이용해 cost가 작은 값으로 갱신하는 과정을 반복함
import sys, heapq
input = sys.stdin.readline

n = int(input())


length = list(map(int, input().split())) + [0]
cost = list(map(int, input().split()))

answer = cost[0] * length[0]
money = cost[0]

for i in range(1, n):
    if cost[i] < money:
        answer += cost[i] * length[i]
        money = cost[i]
    else:
        answer += money * length[i]

print(answer)
    




