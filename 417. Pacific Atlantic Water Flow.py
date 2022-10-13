class Solution(object):
    def pacificAtlantic(self, heights):
        answer = list()

        def dfs(i, j, prev_sea_level):
            if ocean_touch[0] and ocean_touch[1]:
                return

            if i < 0 or j < 0:
                ocean_touch[0] = True
                return

            if i >= len(heights) or j >= len(heights[i]):
                ocean_touch[1] = True
                return

            if prev_sea_level < heights[i][j]:
                return

            if (i, j) in visit:
                return

            visit.append((i, j))

            dfs(i-1, j, heights[i][j])
            dfs(i+1, j, heights[i][j])
            dfs(i, j-1, heights[i][j])
            dfs(i, j+1, heights[i][j])

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                ocean_touch = [False, False]
                visit = list()

                dfs(i, j, heights[i][j])

                if ocean_touch[0] and ocean_touch[1]:
                    answer.append([i, j])

        return answer