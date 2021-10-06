# 괄호 회전하기
# 대괄호, 중괄호, 소괄호로 이루러진 문자열 s가 매개 변수로 주어짐
# s를 왼쪽으로 x칸만큼 회전시켰을 때에 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 반환하시오
from collections import deque

def check(string):
    s = []
    for i in range(len(string)):
        s.append(string[i])
    start = ['(', '{', '[']
    match = {')':'(', '}':'{', ']':'['}
    q = deque()
    while s:
        curr = s.pop(0)
        if curr in start:
            q.append(curr)
        else:
            if q:
                if q[-1] == match[curr]:
                    q.pop()
                else:
                    return False
            else:return False
    return True
def spin(s, x):
    """x만큼 회전시킨 문자열 s를 반환"""
    return s[x:] + s[:x]


def solution(s):
    answer = 0
    """길이가 홀수이면 올바른 괄호가 될수 없음"""
    if len(s) % 2 != 0:
        return answer
    else:
        for i in range(len(s)):
            new = spin(s,i)
            if (check(new)) == True:
                answer += 1

    return answer

s = ["[](){}","}]()[{","[)(]","}}}"]
for string in s:
    print(solution(string))