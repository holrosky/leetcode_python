import heapq

class Solution:
    def k_smallest_pairs(self, nums1, nums2, k):
        res = []
        heap = []
        visited = set()

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        visited.add((0, 0))

        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return res


solution = Solution()
print(solution.k_smallest_pairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
print(solution.k_smallest_pairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))
print(solution.k_smallest_pairs(nums1 = [1,2], nums2 = [3], k = 3))
