from heapq import heappush, heappop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        ladder_heap = []

        for i in range(len(heights) - 1):
            height_to_jump = heights[i + 1] - heights[i]

            if height_to_jump <= 0:
                continue

            heappush(ladder_heap, height_to_jump)

            if len(ladder_heap) <= ladders:
                continue

            bricks -= heappop(ladder_heap)

            if bricks < 0:
                return i

        return len(heights) - 1


solution = Solution()
print(solution.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
print(solution.furthestBuilding([14, 3, 19, 3], 17, 0))
