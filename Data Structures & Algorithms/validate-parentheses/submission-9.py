class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False


        close = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        stack = []

        for bracket in s:
            if bracket in close:
                if not stack:
                    return False
                if stack.pop() != close[bracket]:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False

        return True