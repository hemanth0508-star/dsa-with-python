'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

s = "anagram"
t = "nagaram"

s=sorted(s)
t=sorted(t)
if s==t:
    print("True")
else:
    print("False")
    

