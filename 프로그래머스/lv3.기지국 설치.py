#Sol1. 효율성 제외 정확도 까지만 통과
def solution(n, stations, w):
    answer = 0
    div = w*2+1
    flag = [0]*n
    stations = list(map(lambda x:x-1, stations))
    for i in stations:
        left = max(0, i-w)
        right = min(n, i+w+1)
        for k in range(left, right):
            flag[k] = 1
    while True:
        if 0 not in flag:
            break
        else:
            temp = flag.index(0)
            count = 0
            while temp < n and flag[temp] == 0:
                flag[temp] = 1
                count += 1
                temp += 1
            if count % div == 0:
                answer += count//div
            else:
                answer += 1 + count//div
    return answer
    
    
#Sol2. 효율성 까지 통과
#flag라는 배열을 이용해서 현재 수신이 가능한 지역을 매번 station에 있는 모든 기지국 마다 수행하고 while문을 돌리니 시간 초과 발생
#따라서 그냥 index의 값을 이용해서 갱신
#math.ceil()로 올림함수를 이용해서 현재 각 구간 길이마다 갱신해야 하는 기지국의 최소 개수를 구했다.
import math
def solution(n, stations, w):
    answer = 0
    div = w*2+1
    before = 0
    for i in stations:
        if before == n:
            break
        left = max(0, i-w)
        right = min(n, i+w)
        count = left-before-1
        #여기서 계속 if count == 0:break를 이용해서 틀렸었다.
        #왜냐하면 station에 있는 모든 경우는 모두 살펴 보아야 하기 때문이다. 단순히 양끝값이 일치했기 떄문에 구간의 길이가 0인 것으로, n개의 기지국 모두를 사용 가능하다는 뜻이 아니다.
        answer += math.ceil(count/div)
        before = right
    if before < n:
        count = n-before
        answer += math.ceil(count/div)
    return answer
