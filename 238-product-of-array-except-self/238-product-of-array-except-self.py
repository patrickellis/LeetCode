class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = list(nums)
        rightProducts = list(nums)
        for i in range(1,len(nums)):
            leftProducts[i]*=leftProducts[i-1]
            right_index = len(nums)-1-i
            rightProducts[right_index]*=rightProducts[right_index+1]
        for i in range(1,len(nums)-1):
            nums[i] = leftProducts[i-1]*rightProducts[i+1]
        nums[0]=rightProducts[1]
        nums[-1]=leftProducts[-2]
        return nums