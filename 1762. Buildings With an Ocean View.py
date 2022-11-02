from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        for current in range(n):
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)

        return answer


solution = Solution()
print(solution.findBuildings([4,2,3,1]))
print(solution.findBuildings([4,3,2,1]))
print(solution.findBuildings([1,3,2,4]))
