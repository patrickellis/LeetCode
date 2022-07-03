# Time Complexity: O(N^2) - for each number, run a two pointers algorithm on the remainder of the
# input array.
# Space Compleixty: O(1) - no data structures required except for the array holding the answer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        # We know that our algorithm is going to run in 
        # O(N^2) time
        # Therefore, sorting the input comes at no cost
        nums.sort() 
        res = []
 
        
        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            # initialise left and right pointers
            l, r = i+1, len(nums)-1
            
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
        return res
            
        