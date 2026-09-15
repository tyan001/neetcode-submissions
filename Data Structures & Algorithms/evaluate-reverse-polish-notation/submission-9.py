class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for char in tokens:
            if char[0]=='-' and len(char)>1:
                stack.append(int(char))
            elif char.isdigit():
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                val = self.do_operation(char, num1, num2)
                stack.append(int(val))
        
        return int(stack.pop())
        
    def do_operation(self, char: str, operand1:int, operand2:int)->int:

        if char in "+":
            return operand1 + operand2
        elif char in "-":
            return operand1 - operand2
        elif char in "*":
            return operand1 * operand2
        elif char in "/":
            return operand1 / operand2
        else:
            print(f"operand don't exist")
            print(char)
            return 0
        
        
