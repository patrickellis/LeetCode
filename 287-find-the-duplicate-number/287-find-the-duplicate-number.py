class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # let's use a trick
        # for each num in nums,
        # times the number at that index by -1
        # if we are trying to flip a number that is already negative
        # we have discovered our duplicate
        for n in nums: 
            if nums[abs(n)] < 0: return abs(n)
            nums[abs(n)] *= -1
        return -1
    
    
    # [1,3,4,2,2]
    # [1,-3,4,2,2]
    # [1,-3,4,-2,2]