class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # For as long as the current sum is non-negative
        # we are better off continuing the previous sum than beginning
        # a new one. 
        res = -float('inf')
        running_sum = 0
        
        for n in nums:
            continued_sum = running_sum + n
            running_sum = continued_sum if running_sum >= 0 else n
            res = max(res,running_sum)
        return res