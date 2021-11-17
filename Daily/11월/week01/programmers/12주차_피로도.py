answer = -1
def graph(order, k,dungeons):
    global answer
    count = 0
    left = k
    for o in order:
        need, use = dungeons[o][0], dungeons[o][1]
        if left < need:break
        else:
            count += 1
            left -= use

    answer = max(answer, count)

    
    
def solution(k, dungeons):
    global answer
    from itertools import permutations
    choices = list(permutations(list(i for i in range(len(dungeons))),len(dungeons)))
    for c in choices:
        graph(c, k, dungeons)

    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))
