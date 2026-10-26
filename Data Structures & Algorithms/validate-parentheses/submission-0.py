class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs ={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return(False)
                    break
                else:
                    stack.pop() 

        else:
            return(len(stack) == 0) 