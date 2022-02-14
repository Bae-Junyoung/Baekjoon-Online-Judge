bracket = input()

stack = [bracket[0]]
tmp = 2 if bracket[0]=='(' else 3
answer = 0

for i in range(1,len(bracket)):
    if bracket[i]==']':
        if not stack or stack[-1]=='(':
            answer=0
            break
        elif bracket[i-1]=='[':
            answer += tmp
            stack.pop()
        else:
            stack.pop()

        tmp //= 3
        
    if bracket[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        elif bracket[i-1]=='(':
            answer += tmp
            stack.pop()
        else:
            stack.pop()
        tmp //= 2
        
    if bracket[i]=='(':
        stack.append('(')
        tmp *= 2
    if bracket[i]=='[':
        stack.append('[')
        tmp *= 3
    
if len(stack)!=0:
    print(0)
else:
    print(answer)