class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1; r = n-1;
            
            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                
                if total_sum < 0:
                    l += 1
                elif total_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
        return res