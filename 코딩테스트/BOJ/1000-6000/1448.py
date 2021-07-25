import sys
input = sys.stdin.readline
# 그냥 단순히 3중 for문으로 돌리게 되면 시간 초과 발생
def tri(lengths):
    lengths = sorted(lengths)
    a, b, c = lengths[0], lengths[1], lengths[2] # min -> max
    if c < a+b:
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    answer = -1
    data = []
    for _ in range(n):
        data.append(int(input()))
    data = sorted(data, reverse = True)

    # 역순으로 우선 정렬을 해 준 뒤에 삼각형의 결정조건을 이용하기 위해
    while len(data) >= 3:
        # 현재 리스트에서 제일 긴 3개의 길이
        # 만약에 a가 b+c보다 길다면 나머지 경우는 당연히 삼각형이 만들어지지 않기 때문에 
        # 이상황에서 break를 해야 한다.
        a, b, c = data[0], data[1], data[2]
        if tri([a, b, c]) == False:
            data.pop(0)
        else:
            answer = a+b+c
            break

            
    print(answer)
                    


    