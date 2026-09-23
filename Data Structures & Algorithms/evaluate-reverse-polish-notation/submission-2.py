class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1+temp2)
            elif tok == "-":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1-temp2)
            elif tok == "*":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1*temp2)
            elif tok == "/":
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(int(temp1/temp2))
            else:
                stack.append(int(tok))
        
        return (stack[0])