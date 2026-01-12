from collections import deque
stack=deque()

print(stack)
stack.append(5)
print(stack)
stack.pop()
print(stack)
if len(stack)>0:
  print(stack[-1])
else:
  print("stack is empty")