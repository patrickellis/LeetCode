class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        if n == 3: return 1        
        prime = [True for i in range(n)]
        prime[0] = prime[1] = False        
        res = 1
        
        for i in range(3, n, 2):
            if prime[i]:
                res += 1
                for j in range(i*2, n, i):
                    prime[j] = False
        return res
        