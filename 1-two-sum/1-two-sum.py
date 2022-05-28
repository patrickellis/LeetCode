class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, x in enumerate(nums):
            if target - x in seen:
                return [seen[target-x],index]
            seen[x] = index
        return []