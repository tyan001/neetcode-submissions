# # Originally thought the code was trying not to keep track of a min val for practice.
# class MinStack:

#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
        
#         temp = []
#         minVal = self.top()
#         while len(self.stack):
#             minVal = min(minVal, self.top())
#             temp.append(self.stack.pop())
        
#         while len(temp):
#             self.push(temp.pop())
        
#         return minVal

# This one is with keeping track of min
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
         return self.minStack[-1]
