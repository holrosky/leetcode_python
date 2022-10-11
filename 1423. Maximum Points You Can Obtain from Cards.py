from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_score = 0
        right_score = 0
        n = len(cardPoints)

        for i in range(k):
            left_score += cardPoints[i]

        max_score = left_score

        for i in range(k - 1, -1, -1):
            left_score -= cardPoints[i]
            right_score += cardPoints[n - (k - i)]
            current_score = left_score + right_score
            max_score = max(max_score, current_score)

        return max_score


solution = Solution()
print(solution.maxScore([1,2,3,4,5,6,1], 3))
