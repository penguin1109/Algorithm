# 쿼드압축 후 개수 세기
class Main():
    def square(self, start_x, start_y, n,arr):
        global answer
        if n == 1:
            if arr[start_y][start_x] == 0:
                answer[0] += 1
                return
            else:
                answer[1] += 1
                return
        else:
            first = arr[start_y][start_x]
            valid = True
            for x in range(start_x, start_x + n):
                for y in range(start_y, start_y + n):
                    if first != arr[y][x]:
                        valid = False
                        break
            if valid:
                if first == 0:
                    answer[0] += 1
                    return
                else:
                    answer[1] += 1
                    return
            else:
                dx, dy = [0,n//2,0,n//2],[0,0,n//2,n//2]
                for i in range(4):
                    self.square(start_x+dx[i], start_y+dy[i], n//2, arr)
        return
    def solution(self, arr):
        global answer
        n = len(arr)
        self.square(0,0,n,arr)
        return answer

arr = [[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]],[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]]
main = Main()
for a in arr:
    answer = [0,0]
    print(main.solution(a))