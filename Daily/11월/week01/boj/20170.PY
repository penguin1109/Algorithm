from heapq import *
import sys
input = sys.stdin.readline


first = sorted(list(map(int, input().split())))
second = sorted(list(map(int, input().split())))

s = 0
f =0
answer = 0
temp = 0
while (f < 6):
    fv = first[f]
    count = 0
    while (f < 6 and first[f] == fv):
        f += 1
        count += 1
    while (s<6 and second[s] <= fv):
        if (second[s] < fv):
            s += 1
            temp += 1
        else:
            s += 1
    
    answer += (count * temp)
    temp = s



def frac(a, b):
    for i in range(a, 1, -1):
        if (a %i == 0 and b%i == 0):
           a //= i
           b //= i
    return str(a) + '/' +str(b)

result = frac(answer, 36)
print(result) 