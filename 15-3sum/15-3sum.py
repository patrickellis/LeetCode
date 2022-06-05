def print_array(nums):
    for n in nums:
        print("{} ".format(n), end="", flush=True)
    print("")
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        i = 0
        n = len(nums)
        nums.sort()
        print_array(nums)
        while i < n-2:            
            while i > 0 and nums[i] == nums[i-1] and i < n-1: i+=1 
            l = i+1
            r = n-1
            while l < r:
                # while l < r-1 and nums[l] == nums[l+1]: l+=1
                # while r > l+1 and nums[r] == nums[r-1]: r-=1
                triplet_sum = nums[i] + nums[l] + nums[r]
                # print("triplet_sum: {} + {} + {} = {}".format(
                #     nums[i],
                #     nums[l],
                #     nums[r],
                #     triplet_sum
                # ))
                if triplet_sum < 0:
                    l+=1
                elif triplet_sum > 0:
                    r-=1
                else:
                    result.add((nums[i],nums[l],nums[r]))
                    l+=1
            i+=1
        return [list(tuple_) for tuple_ in result]