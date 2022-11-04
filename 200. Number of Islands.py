class Solution(object):
    def numIslands(self, grid):
        count = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    count += 1

                    self.dfs(grid, m, n)

        return count

    def dfs(self, grid, m, n):
        if grid[m][n] == '1':
            grid[m][n] = '#'
            if m + 1 < len(grid):
                self.dfs(grid, m + 1, n)
            if n + 1 < len(grid[0]):
                self.dfs(grid, m, n + 1)
            if m - 1 >= 0:
                self.dfs(grid, m - 1, n)
            if n - 1 >= 0:
                self.dfs(grid, m, n - 1)

solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))