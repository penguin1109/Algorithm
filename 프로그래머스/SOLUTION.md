#### PROGRAMMERS LV3.최고의 집합
- 자연수 n개로 이루어진 중복 집합 중에  
  1. 각 원소의 합이 s가 되는 수의 집합
  2. 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합
  3.위 두 조건을 만족하는 집합을 최고의 집합이라고 한다.
  4. 집합의 원소의 개수 n과 모든 원소들의 합 s가 주어진다.  
- 처음에는 그냥 무턱대고 백트래킹으로 풀었고, 답은 나왔으나 당연히 시간 초과가 발생하였다.
- 그러나 생각해보니 **최대의 곱**을 갖기 위해서는 원소로 주어지는 수가 커야 하며, 임의의 실수가 아닌 변수를 대입하였을 때 n개로 s라는 합을 만드는 수들의 집합의 곱은 s//n, 즉 모든 수가 이왕이면 일치할 수록 크다는 것을 수학적 접근을 통해 알 수 있었다.
  - 따라서 그렇게 while 반복문을 s > 0 이고 n > 0일 때까지 돌려주면 문제 없이 해결이 가능하다.
```py3
def solution(n,s):
    answer = [-1]
    temp = []
    while (s>0 and n>0):
        if s%n == 0:
            for _ in range(n):
                temp.append(s//n)
            s,n = 0,0
        else:
            a = s//n
            temp.append(a)
            n -= 1
            s -= a

    if temp == []:
        return [-1]
    else:
        return temp 
```

#### PROGRAMMERS LV3. 야근지수
- 퇴근까지 남은 n 시간동안 남은 일 works를 리스트로 걸리는 시간을 받는데, 여기서 야근 피로도를 최소화하도록 일을 한다.
- 그리고 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량의 제곱합이다.
- 여기서 앞 문제와 조금은 비슷하게 풀면 되는데, 수학적으로 접근 하여 처음에는 마지막 return 값은 sum(lambda x:x**2, works)로 했는데 이렇게 하려면 **매번 works리스트의 최댓값에서 1을 빼주어야 한다.
  - 따라서 효율성 테스트를 통과 못하는 경우가 발생하여 n^2 - (n-1)^2 = 2*n-1임을 이용하여 answer을 갱신하고
  - 항상 다음 최댓값은 무조건 이전 최댓값에서 1을 뺀 값이 될 테니 counted에 다음 최댓값을 갖는 원소의 개수를 더해주는 방법으로 갱신하여 works 리스크를 굳이 수정할 필요가 없게 된다.
  
```py3
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    else:
        temp = max(works)
        answer = sum(map(lambda x:x**2, works))
        counted = 0
        while (n>=0):
            counted += works.count(temp)
            if n > counted:
                answer -= counted*(2*temp-1)
                n -= counted
            else:
                answer -= n*(2*temp-1)
                return answer
            temp -= 1
    return answer
```    