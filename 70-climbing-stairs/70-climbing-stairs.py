class Solution:    
    def climbStairs(self, n: int) -> int:
        self.memo = [-1 for i in range(n+1)]
        self.memo[0] = self.memo[1] = 1
        res = self.climbStairsOptimized(n)    
        return res
    
    def climbStairsOptimized(self,n: int) -> int:
        if(n < 0): return 0
        if self.memo[n] != -1: return self.memo[n]
        result = self.climbStairsOptimized(n-1) + self.climbStairsOptimized(n-2)
        self.memo[n] = result
        return result