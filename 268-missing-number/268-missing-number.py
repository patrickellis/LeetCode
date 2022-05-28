class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we can solve this mathematically
        # or we can solve it programmatically
        # mathematical first:
        n = len(nums)
        return int((n*(n+1))/2 - sum(nums))