s="A man, a plan, a canal: Panama"

res=[i.lower() for i in s if i.isalnum()]
rev=res[::-1]
if rev==res:
    print("given string is a valid palindrome")
else:
    print("given string is not a valid palindrome")
    
'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''