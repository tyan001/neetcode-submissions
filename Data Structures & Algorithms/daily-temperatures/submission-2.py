class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        stack = []  # indices of still-live candidates

        for i in range(n - 1, -1, -1):
            # everything not warmer than i is dead — i blocks it forever
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i   # nearest surviving candidate

            stack.append(i)

        return res

        
            