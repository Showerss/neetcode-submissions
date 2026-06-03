class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mappings = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        if len(s) == 0:
            return False

        for i in s:
            if i in mappings:
                stack.append(i)
            elif not stack or mappings[stack.pop()] != i:
                return False 
        
        return not stack