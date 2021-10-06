import sys
<<<<<<< HEAD
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n -> 배열의 크기 m -> 숫자가 더해지는 횟수 
# 주어진 수들을 m번 더해서 배열의 특정 index가 k번 이상 더해지지 않아서 만들 수 있는 제일 큰 수를 구하여라

nums = list(map(int, input().split()))

answer = 0
nums.sort(reverse = True)
fir, sec = nums[0], nums[1]

rep, more = m//(k+1), m%(k+1)

answer = (fir*k+sec) * rep + fir * more

print(answer)
=======
# defaultdict를 사용하면 key에 없는 값을 입력하려고 할 때에 자동으로 정해준 자료형에 맞는
# 숫자로 기본 값으로 입력
from collections import defaultdict
input = sys.stdin.readline

# 0과 1로만 이루어진 문자열
# 문자열을 모두 같은 수로 만들기 위한 최소의 뒤집는 횟수

def answer(x, y):
    print('Case #%s: %s'%(str(x), str(y)))

if __name__ == "__main__":
    for t in range(int(input())):
        n, c = map(int, input().split())
        intervals = []
        # 주어지는 구간 저장
        for _ in range(n):
            a, b = map(int, input().split())
            intervals.append((a,b))
        
        # a+1로 자를수 있으며 b로는 자를 수 없음
        # 특정 x로 잘랐을때 나오는 조각의 개수를 사전형에 저장
        checks = defaultdict(int)
        for a, b in intervals:
            checks[a+1] += 1
            checks[b] -= 1

        cuts = []
        curr, prev = 0,0
        for k in sorted(checks.keys()):
            # 조각 갱신
            cuts.append((curr, k-prev))
            curr += checks[k]
            prev = k
        
        ans = 0
        for lap, length in reversed(sorted(cuts)):
            to_cut = min(c, length)
            ans += lap * to_cut
            c -= to_cut
            if c == 0:break
            
        answer(t+1, ans)
    

        
>>>>>>> 166c12fb63db4b9f03e68b83844a0c12ea765459
