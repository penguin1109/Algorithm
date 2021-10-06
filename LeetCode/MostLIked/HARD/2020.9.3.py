#1. Median of Two Sorted Arrays
#문제 자체는 그냥 두개의 리스트가 주어졌을 때에 이를 오름차순으로 합쳤을때 중앙값을 구하는 것이다.
#그냥 각각의 리스트를 정렬을 한 뒤에 양쪽 리스트의 더 작은 값을 merged list에 순서대로 넣는 방법으로 진행을 했다.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        merged = []
        while nums1 and nums2:
            left, right = nums1[0], nums2[0]
            if left < right:
                merged.append(left)
                nums1.pop(0)
            else:
                merged.append(right)
                nums2.pop(0)
        if nums1:
            merged = merged + nums1
        if nums2:
            merged= merged + nums2
        if len(merged) == 1:
            return merged[0]
        else:
            n = len(merged)
            #여기서 마지막 평균갑을 구할때 //2로 했더니 계속 답이 다르게 나왔었음
            if n % 2== 0:return (merged[n//2]+merged[(n//2)-1])/2
            else:return merged[n//2]


#2. Longest Palindromic String
#처음에는 간격을 정해서 left, right값을 for문으로 지정해 줬었는데, 하다 보니까 시간초과가 자꾸났다.
#그래서 만약에 특정 시작점부터 해서 팰린드롬이 없으면 바로 멈추는 방법으로 했다.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = 1
        result = ''
        for i in range(len(s)):
            for j in range(len(s)-i):
                k = i+j
                if k == j:
                    result = s[k]
                if k != j:
                    left, right = j,k
                    ok = True
                    while left < right:
                        if s[left] == s[right]:
                            left += 1
                            right -= 1
                        else:
                            ok = False
                            break
                    if ok:
                        if len(result) < i+1:
                            result = s[j:k+1]
                    else:
                        continue
                        
        return result
#그러나 이렇게 했더니 시간 초과가 발생했고, 따라서 방법을 바꾸어서 dp로 풀기로 했다.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        ans = ''
        for i in range(len(s)):
            for j in range(len(s)-i):
                k = i+j
                if k == j:
                    ans = s[k]
                else:
                    if s[k] == s[j]:
                        if i == 1:
                            dp[j][k] = 1
                            ans = s[j:k+1]
                        else:
                            if dp[j+1][k-1] == 1:
                                dp[j][k] = 1
                                ans = s[j:k+1]
        return ans
#dp로 푼 결과는 성공이었고, 3488ms만에 통과가 되었다.
#알고리즘은 단순하게 dp[i][j]는 s의 i부터 j가 palindrome인지의 여부를 저장하는 것이고,
#중요한 것은 반드시 사이 간격이 좁게 시작해야 하므로 for문에서 두 인덱스 사이의 간격도 먼저 정해 주었다.

#마지막으로 그냥 문자열의 [::-1]을 해서 같은지 아닌지 따졌는데 시간 초과가 없었다.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if len(m) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
#시간 초과가 없던 이유는 현재 제일 긴 문자열 정답보다 짧은 길이라면 무조건 break를 했기 때문이다.
#뿐만 아니라 마지막 자리를 제일 끝부터 내림차순으로 한거라 pandilome이 있므녀 또 break를 했다.    
