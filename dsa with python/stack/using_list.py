l=[]
def push(item):
    l.append(item)

def pop():
    if l is not None:
        return l.pop()
    
def show():
    if len(l)>0:
      return l[-1]
    else:
        return "stack is empty"

print(l)
push(5)
# push(6)
pop()
print(show())