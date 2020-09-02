###Longest Substring Without Repeating Characters

#1.처음에는 'two pointer'을 이용해서 시간 초과가 발생했다.
#그냥 단순하게 0<= i < len(s), i+1 <= j <= len(s)로 정해서 했는데
#여기서 생각을 더 해보니까 만약에 특정 시작 포인터에서 안되는 경우가 발생했다면 그게 끝이니까 끝 포인터를 더인상 티울 필요가 없는 것읻.
#이걸 보완한게 'sliding window'이고, 그걸로 풀어서 통과가 되었다.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:ans = 0
        else:ans = 1
        for i in range(len(s)):
            ok = True
            temp = set()
            idx = i
            while ok and idx < len(s):
                if s[idx] in temp:
                    ok = False
                    ans = max(ans, len(temp))
                else:
                    temp.add(s[idx])
                    idx += 1
            ans = max(ans, len(temp))
        return ans


#2. 다른 풀이(dict()이용하기)

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        start,maxlength= 0,0
        for i, value in enumerate(s):
            #중복되는 문자가 중요하기 때문에 문자를 key로 사전형 자료에 정리한다.
            #가장 최근에 나온 해당 문자의 위치를 dicts에 값으로 저장한다.
            if value in dicts:
                #현재 시작 위치보다 뒤의 위치이면 start값 갱신
                start = max(start,dicts[value]+1)
            #사전형 자료에 저장된 위치 갱신
            dicts[value] = i
            maxlength = max(maxlength, i-start+1)
        return maxlength



###Add Two Numbers
#연결 노드에 관한 문제였다.
#single-linked-list는 정의하면
class ListNode:
    def __init__(self, val = 0, next = None):
        #__init__는 연결 리스트를 초기화한, 그러니까 아무 것도 들어있지 않은 연결리스트를 호출한다.
        
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #정답으로 반환할 result의 head node를 0으로 바꾼 리스트 노드 생성
        result = ListNode
        result_tail = result
        carry = 0
        
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            #l1과 l2에 있는 각 수를 처음부터 더해서 10을 넘으면 carry변수에 10으로 나눈 몫을 전해서 이어서 다음 자리 더할 때 반영

            temp = n1+n2+carry
            carry,out = temp//10, temp%10
            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            #다음 노드가 있으면 정의 아니면 None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next
        
