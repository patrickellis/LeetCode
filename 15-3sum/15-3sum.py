class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We know that our algorithm is going to run in 
        # O(N^2) time
        # Therefore, sorting the input comes at no cost
        nums.sort() 
        res = []
        n = len(nums)
        i = 0
        while(i < n):
            # skip duplicates for first number
            while i > 0 and i < n and nums[i] == nums[i-1]: 
                i+=1
            
            # initialise left and right pointers
            l, r = i+1, n-1
            
            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                if total_sum < 0:
                    l+=1
                elif total_sum > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1; r-=1;
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while r > l and nums[r] == nums[r+1]:
                        r-=1
            i+=1
        return res
            
        