class Solution:
    def isValid(self, s: str) -> bool:
        types = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        brack_stack = []

        for bracket in s:
            if bracket in types:
                if brack_stack and brack_stack[-1]==types[bracket]:
                    brack_stack.pop()
                else:
                    return False
            else:
                brack_stack.append(bracket)
        
        if not brack_stack:
            return True
        else:
            return False


        