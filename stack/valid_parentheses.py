'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
s = "()[]{}"

pairs={")":"(","}":"{","]":"["}
stack=[]
for i in s:
    if i=="(" or i=="{" or i=="[":
        stack.append(i)
    else:
        val=pairs[i]
        if stack:
            if stack[-1]!=val:
                print("False")
                break
            else:
                stack.pop()
        else:
            print("False")
            break
if len(stack)!=0:
    print("False")
else:
    print("True")
        