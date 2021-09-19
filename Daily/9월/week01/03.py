# 위클리 코드 챌린지 - 퍼즐 조각 채우기
# table 배열에 있는 상태대로 남아있는 퍼즐 조각들을 game_board의 빈 부분에 채워줌
import sys
input = sys.stdin.readline
# 최대한 많은 퍼즐 조각을 채워 넣을 때에 몇칸이 채워지는가
def solution(game_board, table):
    answer = -1
    
    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))