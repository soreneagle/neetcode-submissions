class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paras = {'(': ')',
                 '{': '}',
                 '[': ']'
                 }

        if len(s) % 2 == 1:
            return False
        else:
            for i in s:
                if i in paras:
                    stack.append(i)
                else:
                    if not stack:
                        return False

                    last_open = stack.pop()
                    if paras[last_open] != i:
                        return False
        return not stack