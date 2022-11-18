class Solution(object):
    def thousandSeparator(self, n):
        return '.'.join(str(n)[::-1][i:i + 3] for i in range(0, len(str(n)[::-1]), 3))[::-1]

solution = Solution()
print(solution.thousandSeparator(n = 987))
print(solution.thousandSeparator(n = 1234))