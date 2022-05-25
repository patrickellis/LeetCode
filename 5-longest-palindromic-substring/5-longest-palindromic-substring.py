class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        res = 0
        res_string = ""
        while(i < n):
            l = i
            r = i
            # skip duplicates
            while(r < n - 1 and s[r] == s[r+1]):
                r+=1
            while(l > 0 and r < n - 1 and s[r+1] == s[l-1]):
                r+=1
                l-=1
            if(r-l+1 > res):                    
                res = max(res,r-l+1)
                res_string = s[l:r+1]
            i += 1
        return res_string
            
            