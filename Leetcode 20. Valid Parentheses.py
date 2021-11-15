class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracket_map = {
            "}": "{", ")" : "(", "]": "["
        }
        opening_brackets = set(["(", "[", "{"])
        
        for x in s:
            if x in opening_brackets:
                stack.append(x)
            elif stack and stack[-1] == bracket_map[x]:
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        else:
            return True
        
# T = O(N)
# S = O(N)
