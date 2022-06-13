class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # in order to solve this, 
        # we should fix one number
        # and then search the rest of the array for comlpementing
        # pairs that together equal 0 
        # we know from two sum that we can find two nums in an array that equal
        # a target in O(n) time
        # which makes the total complexity O(N^2)
        nums.sort()
        res = []
        index = 0
        while index < len(nums) - 2:
            # skip duplicates
            while index > 0 and index < len(nums) and nums[index] == nums[index-1]:
                index += 1
            l = index+1; r = len(nums)-1
            while l < r:
                triplet_sum = nums[index] + nums[l] + nums[r]                
                if triplet_sum > 0:
                    r -= 1
                elif triplet_sum < 0:
                    l += 1
                else:
                    res.append([nums[index],nums[l],nums[r]])    
                    # skip duplicates
                    while l < r and nums[l]==nums[l+1]: l+=1
                    while r > l and nums[r]==nums[r-1]: r-=1
                    l+=1; r-=1;
            index +=1
            
        return res