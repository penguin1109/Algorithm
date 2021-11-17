# 2204 - 도비의 난독증 테스트
import sys
input = sys.stdin.readline
# 정렬하는 함수를 구현해 보도록 하자
alph = list(map(chr, range(97, 123)))
al = dict()

for _ in range(0,len(alph)*2,2):
    i = alph[_//2]
    al[i.upper()] = _
    al[i] = _

def compare(w1, w2):
    idx = 0
    valid = True
    while (idx < min(len(w1), len(w2))):
        a,b = w1[idx], w2[idx]
        if al[a] < al[b]:
            valid = False
            return w1
        elif al[a] == al[b]:
            idx += 1
        else:
            valid = False
            return w2
    # 길이가 더 긴 단어가 사전상으로 뒤에 위치할 것
    if idx == len(w1)-1:return w1
    else:return w2

while True:
    n = int(input())
    if n == 0:
        break
    else:
        first = ''
        for i in range(n):
            if i == 0:
                first = str(input()).strip()
            else:
                first = compare(first, str(input()).strip())
        print(first)

