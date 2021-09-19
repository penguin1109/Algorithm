# 7주차 - 입실퇴실
# 총 n명이 입실 후 퇴실함
# 입실한 순서가 담긴 배열과 퇴실한 순서가 담긴 배열이 주어질 때에 각각의 사람별로 반드시 만난 사람은 몇명인지
# 번호 순서대로 반환하도록 하는 solution함수를 만드시오
def solution_timelimit(enter, leave):
    answer = [0 for _ in range(len(enter))]
    data = [[0,0]for _ in range(len(enter))]
    for i in range(len(enter)):
        e, l = enter[i], leave[i]
        data[e-1][0] = i
        data[l-1][1] = i
    for i in range(len(enter)):
        for j in range(i+1, len(enter)):
            e, l = data[i][0], data[i][1]
            e_n, l_n = data[j][0], data[j][1]
            if ((e > e_n and l < l_n) or (e < e_n and l > l_n)):
                answer[i] += 1
                answer[j] += 1
            elif (e>e_n and l>l_n) or (e<e_n and l<l_n):
                if (e < e_n and l<l_n):
                    e_temp, l_temp = e, l
                    e, l = e_n, l_n
                    e_n, l_n = e_temp, l_temp
                for k in range(len(enter)):
                    if (k != i and k != j):
                        if data[k][0] > e and data[k][1] < l_n:
                            answer[i] += 1
                            answer[j] += 1
                            break

    return answer
    
def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)]
    ei, li = 0, 0
    room = []
    # 특정 인물이 입장을 했을때에 방에 있던 사람들은 반드시 만날 수 밖에 없는 상황이다
    while ei < len(enter) or li < len(leave):
        if leave[li] not in room:
            answer[enter[ei]] = room[:]
            room.append(enter[ei])
            ei += 1
        else:
            room.remove(leave[li])
            li += 1
    for idx, p in enumerate(answer):
        for m in p:
            answer[m].append(idx)
    return [len(set(i)) for i in answer[1:]]
