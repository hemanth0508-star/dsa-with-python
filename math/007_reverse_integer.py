'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 '''
x=-123
temp=x
if x<0:
  x*=-1
i=0
while x:
  rem=x%10
  i=i*10+rem
  x//=10
if temp<0:
  i*=-1g
if i < -2**31 or i > 2**31 - 1:
  print( 0)
print(i)
