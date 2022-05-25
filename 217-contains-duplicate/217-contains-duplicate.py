class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        return len(seen)!=len(nums)