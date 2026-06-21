'''
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
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
        