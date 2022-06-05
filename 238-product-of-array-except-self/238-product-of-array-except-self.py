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
        for i in range(len(nums)):
            print("{} ".format(leftProducts[i]), end="", flush=True)
        print("")
        for i in range(len(nums)):
            print("{} ".format(rightProducts[i]), end="", flush=True)
        return nums