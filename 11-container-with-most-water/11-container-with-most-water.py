class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)
            
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return res