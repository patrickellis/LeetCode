class Solution:
    def isPalindrome(self, s: str) -> bool:
        # SOLUTIONS --- 
        # Two pointers:
        # one moves from left to right, the other from right to left
        # increment left pointer and decrement right pointer until ! l < r
        l = 0
        r = len(s)-1
        s = s.lower()
        while(l < r):
            while (s[l] == " " or not s[l].isalnum()) and l < r:
                l+=1                
            while (s[r] == " " or not s[r].isalnum()) and r > l:
                r-=1                
            if(s[l] != s[r]):
                return False
            l+=1
            r-=1
        return True