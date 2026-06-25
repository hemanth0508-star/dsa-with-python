'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

s = "leetcode"
vowels = "AEIOUaeiou"
v = ""
for ch in s:
    if ch in vowels:
        v = ch + v      

ans = ""
j = 0

for ch in s:
    if ch in vowels:
        ans += v[j]
        j += 1
    else:
        ans += ch

print(ans)
