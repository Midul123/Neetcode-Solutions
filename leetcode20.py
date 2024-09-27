#leetcode20
def isValid(s):
    closeOpen= { ")":"(", "]":"[", "}":"{" }
    stack =[]
    for char in s:
        if char in closeOpen:
            if stack and stack[-1]==closeOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack
print(isValid("()"))