class Solution:
    def isValid(self, s: str) -> bool:

        
        

        result = []

        mapping = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        
        for i in s:
            #if the i is a key, this if statement handles it
            if i in mapping:
                result.append(i)
            
            #if the i is a value, it'll be handled by this 
            elif not result or mapping[result.pop()] != i:
                return False

        return len(result) == 0