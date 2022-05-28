class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = [False for i in range(len(nums)+1)]
        for n in nums:
            seen[n] = True
        for i in range(len(seen)):
            if not seen[i]:
                return i
        return 0