class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # First solution using a hashmap to store last seen indices of characters
        last_seen = [-1 for i in range(128)]
        res = count = 0 
        
        for idx, char in enumerate(s):
            if last_seen[ord(char)] < 0:
                count += 1
            else:
                count = min(count+1,idx-last_seen[ord(char)])
            last_seen[ord(char)] = idx
            res = max(count, res)
        return res