import sys
input = sys.stdin.readline

wheels = [list(map(int, input().strip())) for _ in range(4)]

def rotate(n, d):
    spin, direction = [0 for _ in range(4)], [0 for _ in range(4)]
    spin[n], direction[n] = 1, d
    tempn, tempd = n, d
    
    # 현재 바퀴 기준 오른쪽의 바퀴들과 맞닿아있는 부분 비교
    for i in range(n+1, 4):
        if wheels[tempn][2] != wheels[i][6]:
            spin[i] = 1
            tempd *= -1
            direction[i] = tempd
            tempn = i
        else:
            break

    # 현재 바퀴 기준 왼쪽의 바퀴들과 맞닿아있는 부분 비교
    tempn, tempd = n, d
    for i in range(n-1, -1, -1):
        if wheels[tempn][6] != wheels[i][2]:
            spin[i] = 1
            tempd *= -1
            direction[i] = tempd
            tempn = i
        else:
            break
    
    for i in range(4):
        if spin[i] == 1:
            # 시계 방향
            if direction[i] == 1:
                # 마지막을 맨앞으로
                temp = wheels[i].pop()
                wheels[i] = [temp] + wheels[i]
            # 반시계 방향
            else:
                temp = wheels[i].pop(0)
                wheels[i] = wheels[i] + [temp]



K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    rotate(n-1, d)

answer = 0
for i in range(4):
    if wheels[i][0] == 1:
        answer += 2**i

print(answer)
    




