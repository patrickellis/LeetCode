class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(nums)
        nums.sort()
        while i < n-2:            
            while i > 0 and nums[i] == nums[i-1] and i < n-1: i+=1 
            l = i+1
            r = n-1
            while l < r:                
                triplet_sum = nums[i] + nums[l] + nums[r]
                if triplet_sum < 0:
                    l+=1
                elif triplet_sum > 0:
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: l+=1
                    while r > l and nums[r] == nums[r-1]: r-=1
                    l+=1; r-=1
            i+=1
        return result