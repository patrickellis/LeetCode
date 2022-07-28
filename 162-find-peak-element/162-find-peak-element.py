class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mp = int(l + (r - l) / 2)
            if nums[mp] > nums[mp+1]:
                r = mp
            else:
                l = mp + 1
        return l;