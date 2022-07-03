class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1: O(nlogn)
        # sort the array and compare adjacent elements for equality
        # Solution 2: O(n)
        # Insert into a set, check for existence as we go
        seen = set()
        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False