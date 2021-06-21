def solution(name):
    #answer = 0
    def count(S, D):
        import string
        '''
        S : start alphabet 
        D : destination alphabet
        '''
        alpha = {}
        for i, val in enumerate(list(string.ascii_uppercase)):
            alpha[val] = i
        s, d = alpha[S], alpha[D]
        a,b,c = s, d-s, len(alpha)-d
        return min(a+c, b)
    def moves(name):
        
    name = name.strip()
    answer = []
    move = 0
    for i in range(len(name)):
        answer.append(count('A', name[i]))
    return answer
# 'A'가 연속으로 포함이 된 경우에 예외적으로 생각해볼 부분이 있었다.
name = 	"BBBBAAAABA"
print(solution(name), sum(solution(name)))
#print(sum(solution(name)) + len(name))