'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''
n=1221
temp=n
i=0
while n:
  rem=n%10
  i=i*10+rem
  n//=10
if i==temp:
  print("True")
else:
  print("False")
  
# Input: x = 121
# Output: true
