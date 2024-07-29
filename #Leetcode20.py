#Leetcode20
def isValid(s):
    matching_bracket = {')': '(', '}': '{', ']': '['}
    stack=[]
    for char in s:
        if char in matching_bracket:
            topelement=stack.pop() if stack else '#'
            if matching_bracket[char] != topelement:
                return False
        else:
            stack.append(char)
    return not stack
print(isValid("()"))