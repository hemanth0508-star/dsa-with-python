'''You are given a string s consisting of lowercase English letters ('a' to 'z').
Your task is to:
Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.
Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
The frequency of a letter x is the number of times it occurs in the string.'''
s = "successes"
freq={}
for i in s:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
vowels="AEIOUaeiou"
vowels_freq={}
cons_freq={}
for key in freq:
  if key in vowels:
    vowels_freq[key]=freq[key]
  else:
    cons_freq[key]=freq[key]
max_vowel=0
max_cons=0
for key in vowels_freq:
  if vowels_freq[key]>max_vowel:
    max_vowel=vowels_freq[key]
for key in cons_freq:
  if cons_freq[key]>max_cons:
    max_cons=cons_freq[key]
print(max_vowel + max_cons)

# Input: s = "successes"
# Output: 6
