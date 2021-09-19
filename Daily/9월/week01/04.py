# 4주차 직업군 추천하기
# 개발자가 사용하는 언어와 언어 선호도를 입력하면 그에 맞는 직업군 추천
# 개발자가 사용하는 언어의 언어 선호도와 직업군 언어 점수의 곱의 총합이 제일 높은 직업군을 반환
# 총합이 같은 직업군이 여러개일 경우 이름이 사전순으로 가장 빠른 직업군 반환
def solution(table, languages, preference):
    """
    table : 직업군 언어 점수
    languages : 개발자가 사용하는 언어
    preference : 언어 선호도
    """
    answer = ''
    temp = dict()
    result = 0
    
    for data in table:
        data = data.split(' ')
        pref = data[1:][::-1]
        add = 0
        for l in range(len(languages)):
            if languages[l] in pref:
                add += preference[l] * (pref.index(languages[l])+1)
        if add == result:
            temp[add].append(data[0])
        elif add > result:
            result = add
            temp[add] = []
            temp[add].append(data[0])
    res = temp[result]
    res.sort()
    answer = res[0]
    

    return answer