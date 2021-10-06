### KAKAO_보석 쇼핑
#### two pointer이나 sliding window를 이용하면 해결이 가능한 문제이다.
- 문제 자체는 간단했으나 중간에 헷갈리는 부분도 있었고 심지어 효율성 테스트에서 계속 통과하지 못하는 부분들이 있어서 생각보다는 시간이 오래 걸렸던 것 같다.
- 우선 문제의 해결 과정은 
  1. 모든 종류의 보석의 존재 여부를 확인하려는 구간의 시작 부분과 끝 부분을 two pointer을 이용해서 start, end라는 변수로 지정해 주었다.
    - while문의 탈출 조건은 start나 end값중 하나라도 전체 gems list의 길이를 넘어갈 때 였다.
  2. 모든 종류의 보석을 포함할 때에는 start값을 키워가며 범위를 좁혔다.
    - 이때 만약에 보석의 개수가 0개가 되면 보석의 개수를 저장한 dictionary에서 해당 종류의 보석을 없애 주어야 한다.
  3. 모든 종류의 보석을 포함하지 않을 때에는 end값을 키워가며 범위를 늘렸다.
  4. 이렇게 계속 범위를 늘리고 줄이는 과정을 반복하면서 현재 최단 length보다 짧은 길이가 나오면 length와 answer데이터를 갱신해 주었다.
- 다만 보석의 개수를 저장해주는 데이터를 처음에는 전체 보석 종류의 개수만큼의 길이를 가지는 list구조를 이용했었으나 효율성 테스트에서 계속 실패하는 부분이 생겼다.
- 따라서 dictionary구조를 이용해 주었다.
- python의 collection중 하나인 defaultdict()라는 자료 구조를 사용하면 조금 코드가 간단해 질 수 있는 것 같다.
  - 이는 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해준다.
    - 따라서 일반적인 dictionary를 쓸 때에는 해당 값의 key가 없는지 확인하는 if문을 사용하고 새로운 값을 할당해 주는 등의 과정을 거쳐야 하지만 이 구조를 쓰면 그렇게 할 필요가 없다.
    - ```defaultdict = defaultdict(int)```
    - ```defaultdict = defaultdict(lambda = 0)```
    - 등과 같이 자료형을 불러주면 key값이 없는 경우에 0을 할당해 준다.  
    
```py3
def solution(gems):
    answer = [0,0]
    count = dict()
    n_gems = len(set(gems))
    #gem_idx = {gem : idx for idx, gem in enumerate(list(set(gems)))}
    start, end, length = -1,0,len(gems)+1   #start와 end는 two pointer의 역할을 함
    while (start < len(gems) and end < len(gems)):
        if (len(count) == n_gems):                #조건 만족을 할 때
            if (abs(end-start) < length):         #만약 더 짧은 길이로 가능하다면 
                length = abs(end-start)           #길이 데이터를 갱신해줌
                answer[0] = start + 1             
                answer[1] = end + 1
            count[gems[start]] -= 1
            if count[gems[start]] == 0:           #해당 보석이 현재 구간에서 존재하지 않으면
                del count[gems[start]]
            start += 1                            #start포인터 키우기
            if start == len(gems):break
        else:                                     #조건 만족을 하지 않을 때에는 end값을 키우며 구간 범위 늘리기
            end += 1 
            if end == len(gems):
                break
            if gems[end] in count:
                count[gems[end]] += 1
            else:count[gems[end]] = 1
            
    return answer
        
```    
