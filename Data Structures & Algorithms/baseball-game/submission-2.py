class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        for op in operations:

            if op.startswith('-'):
                if(op[1:].isnumeric()):
                    score.append(int(op))

            if op.isnumeric():
                score.append(int(op))

            if op == "+":
                pop2 = score.pop()
                pop1 = score.pop()
                temp = pop1 + pop2
                score.append(pop1)
                score.append(pop2)
                score.append(temp)
            if op == "D":
                num = score.pop()
                score.append(num)
                score.append(num*2)
            if op == "C":
                score.pop()

            print(score)
        return sum(score)


            
        