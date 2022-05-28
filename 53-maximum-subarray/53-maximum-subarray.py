class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # base case:
        if(len(nums)==1):
            return nums[0]
        # Logical approach:
        # We only ever end a subarray if the total drops below 0
        # otherwise, it's worth continuing the subarray
        # at each step, we can compare the current total with our
        # best sum found so far
        res = nums[0]
        count = nums[0]
        for n in nums[1:]:            
            if count < 0:
                count = n                
            else:
                count += n
            res = max(count,res)
        return res
            
            
