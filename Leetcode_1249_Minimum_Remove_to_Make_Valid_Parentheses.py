class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            else:
                if not stack:
                   indexes_to_remove.add(i)
                else:
                    stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))
        result = []

        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                result.append(c)

        return ''.join(result)

'''
    T = O(N)
    S = O(N)
'''
