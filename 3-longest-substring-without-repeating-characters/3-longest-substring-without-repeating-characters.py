class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # First solution using a hashmap to store last seen indices of characters
        last_seen = dict()
        res = count = 0 
        
        for idx, char in enumerate(s):
            if char not in last_seen:
                count += 1
            else:
                count = min(count+1,idx-last_seen[char])
            last_seen[char] = idx
            res = max(count, res)
        return res