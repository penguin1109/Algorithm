def grade(score):
    if score >= 90:return 'A'
    elif score >= 80:return 'B'
    elif score >= 70:return 'C'
    elif score >= 50:return 'D'
    else:return 'F'

def average(scores,n,self,add):

    my = scores[self]
    count = dict()
    f,l = scores[0], scores[0]
    while scores:
        s = scores.pop()
        f = min(f, s)
        l = max(l, s)
        if s not in count:
            count[s] = 1
        else:count[s] += 1
    if count[my] == 1:
        if (f == my or l == my):
            add -= my
            n -= 1
    return add/n
    
def changeMatrix(scores):
    new = [[]for _ in range(len(scores))]
    for i in range(len(scores)):
        for j in range(len(scores)):
            new[i].append(scores[j][i])
    return new

def solution(scores):
    answer = ''
    scores = changeMatrix(scores)
    for i in range(len(scores)):
        curr = scores[i]
        add = sum(curr)
        avg = average(curr, len(scores), i, add)
        answer += grade(avg)


    return answer