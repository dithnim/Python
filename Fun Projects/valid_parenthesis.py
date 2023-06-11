def isValid(s):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for char in s:
        if char in brackets:
            stack.append(char)
        elif not stack or brackets[stack.pop()] != char:
            return False
    return len(stack) == 0


print(isValid("(}"))
