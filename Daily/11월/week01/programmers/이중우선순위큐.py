from heapq import *

def siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while (pos > startpos):
        continue
def heappopMax(heap):
    """heap(list) : 배열"""
    lastelt = heap.popleft()
    if heap:
        returnitem = heap[-1]

def solution(operations):
    answer = []
    result = []
    qin,qax = [],[]
    for op in operations:
        i1, i2 = op.split(' ')[0], op.split(' ')[1]
        if (i1 == 'I'):
            heappush(qin, int(i2))
            heappush(qax, -int(i2))
            
        elif (i1 == 'D'):
            if not qin and not qax:continue
            if (int(i2) == -1): #최솟값을 삭제
                val = heappop(qin)
                qax.remove(-val)
            else: #최댓값을 삭제
                val = heappop(qax)
                qin.remove(-val)                
    if qin and qax:
        answer = [-heappop(qax), heappop(qin)]
    else: answer = [0,0]
                


    return answer

ops = [["I 16", "D 1"], ["I 7","I 5", "I -5", "D -1"]]
for op in ops:
    print(solution(op))