#Leetcode735
def asteroidCollision(asteroids):
    stack = []
    for num in asteroids:
        while stack and num < 0 and stack[-1] > 0:
            if abs(num)>abs(stack[-1]):
                stack.pop()
                continue
            elif abs(num)==abs(stack[-1]):
                stack.pop()
                break
            else:
                break
        else:
            stack.append(num)
    return stack
print(asteroidCollision([5,10,-5]))