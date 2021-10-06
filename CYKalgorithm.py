# 오토마타 및 형식 언어
# CYK Algorithm 구현
# grammar이 주어질 때 입력받은 문자열이 해당 문법에 의해서 생성이 가능한지 자동화하는 시스템을 만들고자 함

ruleMap = dict()
parseVarMap = dict()
import sys
input = sys.stdin.readline

print("'변수 > symbol / 변수 한쌍'의 형태로 입력하시오")
while True:
    gram = str(input())
    if gram == '\n':
        break
    value, key = gram.split('>') # '>'문자를 기준으로 변수와 symbol을 분리
    key = key.split('\n')[0] # 개행문자 처리
    if key in ruleMap:
        ruleMap[key].append(value)
    else:
        ruleMap[key] = [value]

print('확인하고 싶은 문자열을 입력하시오')
string = str(input()).split('\n')[0] # 확인하고 싶은 문자열 입력
n = len(string)

for idx in range(1, n+1):
    s = string[idx-1]
    if idx*n+idx not in parseVarMap:
        parseVarMap[idx*(n+1)] = ruleMap[s]

# print(parseVarMap)
for i in range(2, n+1): # 현재 탐색하는 문자열의 길이
    for j in range(i, n+1): # 끝 인덱스 값
        # print(parseVarMap)
        l = j-i+1 # 시작 인덱스 값
        key = l*n+j
        # print(key)
        ans = set() # 중복을 없애기 위해 set() 사용
        for k in range(l, j):
            a,b = str(l) + str(k), str(k+1)+str(j) # 앞부분 문자열, 뒷부분 문자열
            a,b = l*n+k, (k+1)*n+j
            # print(a, b)
            A, B = parseVarMap[a], parseVarMap[b]
            if A and B:
                for p in range(len(A)):
                    for q in range(len(B)):
                        aVal, bVal = A[p], B[q]
                        # print(aVal, bVal)
                        if aVal+bVal in ruleMap: 
                            for mem in ruleMap[aVal+bVal]: # value값을 grammar의 value값에서 찾아서 입력 -> 없으면 빈 배열로 입력
                                ans.add(mem)
        parseVarMap[key] = list(ans)

print(parseVarMap)

if 'S' in parseVarMap[1*n + n]:
    print('ACCEPT : 입력한 문자열은 해당 문법으로 생성이 가능하다.')
else:
    print('REJECT : 입력한 문자열은 해당 문법으로 생성이 불가능하다.')





