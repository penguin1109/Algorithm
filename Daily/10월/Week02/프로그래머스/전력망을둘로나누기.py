def union(node,b,status):
    check = [False for _ in range(len(status))]
    check[node] = True
    stack = [node]
    count = 0
    while stack:
        n = stack.pop(0)
        check[n] = True
        count += 1
        for l in status[n]:
            if check[l] == False and l != b:
                stack.append(l)
    return count

import math
def solution(n, wires):
    answer = math.inf
    status = [[]for _ in range(n+1)]
    for l in wires:
        a,b = l[0], l[1]
        status[a].append(b)
        status[b].append(a)
    for w in wires:
        node, b = w[0], w[1]
        u = union(node, b, status)
        answer = min(answer, abs(u-(n-u)))


    return answer




Nums = [9,4,7]
Wires = [[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],	[[1,2],[2,3],[3,4]],[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]
for i in range(3):
    n, w = Nums[i], Wires[i]
    
    print(solution(n,w))