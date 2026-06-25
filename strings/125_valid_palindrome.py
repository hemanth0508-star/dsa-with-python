'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

s="A man, a plan, a canal: Panama"
res=[i.lower() for i in s if i.isalnum()]
rev=res[::-1]
if rev==res:
    print("given string is a valid palindrome")
else:
    print("given string is not a valid palindrome")
    
