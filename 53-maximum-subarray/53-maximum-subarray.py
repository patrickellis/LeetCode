class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -pow(10,5)
        running_sum = -pow(10,5)        
        it = 0
        for num in nums:
            running_sum = max(num, running_sum + num)
            res = max(running_sum, res)
        return res
