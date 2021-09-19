# 5주차 - 모음사전
# 실제 사전처럼 단어들이 저장이 되는 상황이었는데, 이해하기가 조금은 어려웠었다
# 그래서 문제를 조금 더 직관적으로 이해 할 수 있도록 각각을 소숫점 아래 수로 생각해서 크기 순으로 정렬하면 되는것으로 생각했다

def solution(word):
    alphs = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    for i in range(len(word)):
        w = word[i]
        if w == 'A':
            answer += 1
        else:
            for j in range(4, i, -1):
                answer += alphs.index(w) * (5**(j-i))
            answer += alphs.index(w)+1
     
    return answer