class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        if len(s)%2 == 1:
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
                if stack.pop() == close[bracket]:
                    continue
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True