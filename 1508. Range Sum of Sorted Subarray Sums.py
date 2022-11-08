from typing import List

class Solution:
    def range_sum(self, nums: List[int], n: int, left: int, right: int) -> int:

        sum_of_subarray = []

        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                sum_of_subarray.append(sum)

        answer = 0
        sum_of_subarray = sorted(sum_of_subarray)

        for i in range(left - 1, right):
            answer += sum_of_subarray[i]

        return answer % 1_000_000_007


solution = Solution()
print(solution.range_sum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
print(solution.range_sum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
print(solution.range_sum(nums = [1,2,3,4], n = 4, left = 1, right = 10))
