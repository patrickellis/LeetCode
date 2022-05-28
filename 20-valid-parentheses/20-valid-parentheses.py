class Solution:    
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {']':'[', '}':'{', ')':'('}
        for char in s:
            if(char in ["[", "{", "("]):
                stack.append(char)
            else:
                if(not len(stack) or stack[-1] != complement[char]):
                    return False
                stack.pop()
        return not len(stack)
                