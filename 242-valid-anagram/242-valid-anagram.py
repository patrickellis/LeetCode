class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0 for i in range(128)]
        str_length = len(s)
        for i in range(str_length):
            count[ord(s[i])]+=1
            count[ord(t[i])]-=1
        for i in range(128):
            if(count[i] != 0):
                return False
        return True
            