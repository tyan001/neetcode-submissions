class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_key = { '}':'{', ']':'[', ')':'('}

        stack = []

        for bracket in s:

            if bracket in bracket_key:
                if not stack:
                    return False
                if stack.pop() != bracket_key[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
            
        return True
                
