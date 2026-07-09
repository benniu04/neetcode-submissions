class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in valid.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    element = stack.pop()
                    if element == "(" and i != ")":
                        return False
                    elif element == "[" and i != "]":
                        return False
                    elif element == "{" and i != "}":
                        return False
        
        return len(stack) == 0
            