
s="leetcode"
vowels="AEIOUaeiou"
i=0
j=len(s)-1
s=list(s)
while i<j:
    if s[i] not in vowels:
        i+=1
    if s[j] not in vowels:
        j-=1
    if s[i] in vowels and s[j] in vowels:
        if i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
s=''.join(s)
print(s)
        
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