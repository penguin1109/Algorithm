# 최소 직사각형
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때에 지갑의 크기를 return
import math
class Main():

    def check(self, cycle,w,h, sizes):
        global result
        if (cycle == len(sizes)):
            result.append(w*h)
            return
        else:
            W, H = sizes[cycle][0], sizes[cycle][1]
            self.check(cycle+1, max(w, W), max(h, H), sizes)
            self.check(cycle+1, max(w,H), max(h, W), sizes)

    def solution(self, sizes):
        """가로와 세로의 길이라고 제공해주는 것의 의미가 특별히 있는 상황이 아니기 때문에
        입력값을 비교해서 더 짧은 길이를 무조건 가로, 더 긴 길이를 세로로 설정해서
        각각의 가로와 세로에서 최댓값의 곱이 답이다"""
        big_w, big_h = 0,0
        for s in sizes:
            w, h = s[0], s[1]
            if w > h:
                s = [h, w]
            big_w = max(big_w, s[0])
            big_h = max(big_h, s[1])
        return big_w*big_h
        
    def solution01(self, sizes):
        """백트래킹과 재귀를 사용해서 모든 경우 탐색 -> 시간 초과 발생"""
        global result
        answer = math.inf
        self.check(0, 0, 0, sizes)
        return min(result)

main = Main()
sizes = [[[60, 50], [30, 70], [60, 30], [80, 40]],[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]
for s in sizes:
    result = []
    print(main.solution(s))