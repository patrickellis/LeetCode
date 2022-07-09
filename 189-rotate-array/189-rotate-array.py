class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # apply fix for if k > len(nums)
       # k = k % len(nums)
        res = []
        
        #  nums = [1,2,3,4,5,6,7], k = 3, len(nums) = 7
        # select idx 7-3 = 4
        # 5, 6, 7
        idx = len(nums)-k
        while(len(res) < len(nums)):            
            idx = idx % len(nums)
            res.append(nums[idx])                     
            idx+=1
            
        for i,v in enumerate(res):
            nums[i] = v