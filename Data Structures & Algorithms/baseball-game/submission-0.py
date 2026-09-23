class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = {"+", "C" , "D"}
        stack = []

        for item in operations:
            if item not in ops:
                stack.append(int(item))
            
            else:
                if item == "+":
                    temp2 = stack.pop()
                    temp1 = stack.pop()
                    temp3 = temp1+temp2
                    stack.append(temp1)
                    stack.append(temp2)
                    stack.append(temp3)
                
                elif item == "C":
                    stack.pop()
                else:
                    temp1 = stack.pop()
                    temp2 = temp1*2
                    stack.append(temp1)
                    stack.append(temp2)
                    
        
        total = 0
        while stack:
            total+= stack.pop()
        
        return total


        