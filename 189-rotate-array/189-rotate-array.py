class Solution:

        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        count = 0
        current = 0
        
        while count < len(nums):
            start = current
            prev = nums[start]
            
            while(True):
                next_ = (start + k) % len(nums)    
                temp = nums[next_]
                nums[next_] = prev
                prev = temp
                start = next_
                count += 1
                if current == start:
                    current += 1
                    break
                    
                