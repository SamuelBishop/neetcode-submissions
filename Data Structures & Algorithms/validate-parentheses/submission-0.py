class Solution:
    def isValid(self, s: str) -> bool:
        # Push onto the stack for these chars
        # Pop off of the stack for these chars

        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False