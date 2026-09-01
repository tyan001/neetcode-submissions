class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        for op in operations:

            if op == "+":
                pop2 = score.pop()
                pop1 = score.pop()
                temp = pop1 + pop2
                score.append(pop1)
                score.append(pop2)
                score.append(temp)
            elif op == "D":
                num = score.pop()
                score.append(num)
                score.append(num*2)
            elif op == "C":
                score.pop()
            else:
                score.append(int(op))

            print(score)
        return sum(score)


            
        