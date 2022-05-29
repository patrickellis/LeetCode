class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # THE GOAL:
        # a one-pass solution
        # the problem:
        # because we are dealing with negative numbers
        # a minimum value can become a maximum value
        # therefore, we NEED to track both current max and min in order
        # to solve this problem optimally
        prev_min = prev_max = res = nums[0]
        for n in nums[1:]:
            curr_1 = prev_min * n
            curr_2 = prev_max * n
            prev_min = min([curr_1, curr_2, n])
            prev_max = max(curr_1, curr_2, n)
            res = max(prev_max,res)
        return res
        