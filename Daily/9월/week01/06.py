# 6주차 - 복서 정렬하기
# 전체 승률이 높은 선수일수록 번호가 앞쪽으로 감
# 다른 선수와 아직 붙어본 적이 없는 선수의 승률은 0
# 승률이 동일한 선수들 중에서는 자신보다 무거운 선수를 이긴 횟수가 많으면 더 앞으로 감
# 무거울수록 번호가 앞으로감 (몸무게는 오름차순)
# 몸무게까지 동일하면 번호는 내림차순
def solution(weights, head2head):
    answer = []
    rates = []
    for idx, info in enumerate(head2head):
        count = len(head2head)
        win = 0
        heavier = 0
        for j in range(len(info)):
            i = info[j]
            # 만약에 경기를 한적이 없다면 전체 시합 횟수에서 1만큼 빼줌
            if i == 'N':count-=1
            # 이긴 적이 있다면 무게가 더 가벼우면 
            elif i == 'W':
                win += 1
                if (weights[idx] < weights[j]):
                    heavier += 1

        if count == 0:rate = 0
        else:rate = win/count
        # 각각의 값들의 우선순위와 오름차순/내림차순을 반영해서
        # 정렬을 sort를 통해서 수행해 준 뒤에 답의 index에 1을 더한 값을 정답으로 반환한다.
        rates.append((-rate, -heavier, -weights[idx], idx))
    rates = sorted(rates)
    for r in rates:
        answer.append(r[-1] + 1)
    

    return answer