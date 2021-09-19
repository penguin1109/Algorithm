# 200. Number of Islands
# BFS (Breath First Search)
class Solution:
    def dfs(self, grid, x, y):
        """
        깊이 우선 탐색을 실행해서 1로 이어지는 섬을 찾아서 "1"로 표시된 부분을
        "0"으로 바꾸어 나중에 탐색을 하지 않도록 한다
        굳이 check배열이 따로 필요가 없다는 점에서 비교적 간단하다는 생각이 들었다.
        물론 bfs의 경우에는 check배열을 갱신하고 다시 원래대로 돌려놓는 과정이 중요하다
        """
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<len(grid) and 0 <= ny<len(grid[0]):
                if grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    self.dfs(grid, nx, ny)

    def numIslands(self, grid):
        """
        전체 주어진 배열의 행과 열의 개수를 각각 우선 구한 뒤에
        "1"이 존재하면 그 부분을 starter index로 설정해서 
        그 위치부터 섬을 찾기 위해서 dfs를 실행한다.
        """
        m = len(grid) # 가로 행의 개수
        n = len(grid[0]) # 세로 열의 개수
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

sol = Solution()
grid =[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))


        