'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
s="anagram"
t="nagaram"
if len(s) != len(t):
    return False
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in t:
    if ch not in freq:
        return False
    freq[ch] -= 1
    if freq[ch] < 0:
        return False
return True
'''
# Example
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
'''
