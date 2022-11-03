class Solution(object):
    def recover_tree(self, root):
        def in_order(r):
            return in_order(r.left) + [r.val] + in_order(r.right) if r else []

        def find_two_nums(nums):
            n = len(nums)
            x = y = None
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == None:
                        x = nums[i]

            return x, y

        def swap_two_nums(r, count):
            if count == 0:
                return

            if r:
                if r.val == y:
                    r.val = x
                    count -= 1
                elif r.val == x:
                    r.val = y
                    count -= 1

                swap_two_nums(r.left, count)
                swap_two_nums(r.right, count)

        nums = in_order(root)
        x, y = find_two_nums(nums)
        swap_two_nums(root, 2)


solution = Solution()
