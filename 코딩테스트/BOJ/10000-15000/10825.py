import sys
input = sys.stdin.readline
# 알파벳은 더 앞이면 , 즉 A>B로 간주
"""
def sort(origin, new):
    sorted = []
    if not origin:
        origin.append(new)
    else:
        for _ in range(len(origin)):
            temp = origin.pop(0)
            for i in range(4):
                if temp[i] < new[i]:
                    origin = [new + temp + origin[0]]
                    break
                elif temp[i] > new[i]:
                    continue
                else:
                    continue
    return origin

if __name__ == "__main__":
    n = int(input())
    origin = []
    for _ in range(n):
        name, a, b, c = map(str, input().split(' '))
        a, b, c = int(a), int(b), int(c)
        new = [a, b, c, name]
        origin = sort(origin, new)
    print(origin)
    for order in range(n):
        print(origin[order][-1])
"""

if __name__ == "__main__":
    n = int(input())
    new = [list(map(str, input().split(' '))) for _ in range(n)]

    new = sorted(map(lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]), new))

    for i in range(n):
        print(new[i][-1])

