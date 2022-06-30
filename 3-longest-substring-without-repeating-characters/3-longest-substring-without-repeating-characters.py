class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1 for i in range(128)]
        res = count = 0 
        
        for idx, char in enumerate(s):
            ord_val = ord(char)
            if last_seen[ord_val] < 0:
                count += 1
            else:
                count = min(count+1,idx-last_seen[ord_val])
            last_seen[ord_val] = idx
            res = max(count, res)
        return res