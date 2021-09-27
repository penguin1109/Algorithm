from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = dict()

    for i in range(len(info)):
        # 4개의 정보와 코딩테스트 점수, 두가지 속성으로 나누어 생각
        other, score = info[i].split()[:-1], info[i].split()[-1]

        for j in range(5):
            # 해당 사용자의 정보에 대해서 가능한 모든 조합을 dictionary의 형태로 저장
            for c in combinations(other, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(score))
                else:
                    info_dict[tmp] = [int(score)]
        
    for k in info_dict:
        info_dict[k].sort()
    
    for q in query:
        q_key, q_score = q.split(' ')[:-1], q.split(' ')[-1]

        while 'and' in q_key:
            q_key.remove('and')
        
        while '-' in q_key:
            q_key.remove('-')

        q_key = ''.join(q_key)

        if q_key in info_dict:
            scores = info_dict[q_key]

            if scores:
                # 이진탐색을 해주는 bisect_left를 사용해서 q_score보다 작은 값의 개수를 정렬된 scores배열에서 찾아줌
                enter = bisect_left(scores, int(q_score))
                answer.append(len(scores)-enter)
        else:
            answer.append(0)
    return answer
