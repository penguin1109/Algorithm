# 숫자를 검색할 때에는 이분 탐색으로 구현
def binary_search(score_list, score):
    l, r = 0, len(score_list)-1
    count = set()
    while l <= r:
        mid = (l+r)//2
        if score_list[mid][0] >= int(score):
            count.add(score_list[mid][1])
            l = mid+1
        else:
            r = mid-1
    return list(count)
        


def search(info, q):
    for j in range(4):
        if (q[j] != '-' and info[j] != q[j]):return False
    return True


def solution(info, query):
    answer = []
    info_list, score_list = [], []
    for idx, i in enumerate(info):
        i = i.split(' ')
        other, score = i[:-1], i[-1]
        info_list.append(other)
        score_list.append((int(score),idx))
    score_list = sorted(score_list)
    print(score_list)
    for q in query:
        count = 0
        q = list(map(lambda x: x.strip(), q.split('and')))
        last = q.pop()
        q.append(last.split(' ')[0])

        index = binary_search(score_list, last.split(' ')[1])
        print(index)
        for j in index:
            if search(info_list[j], q):
                count += 1
        answer.append(count)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))