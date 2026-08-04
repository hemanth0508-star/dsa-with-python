'''Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.
Return the chosen digit as an integer.
The frequency of a digit x is the number of times it appears in the decimal representation of n.'''
n = 1553322
freq={}
while n:
  rem=n%10
  if rem in freq:
    freq[rem]+=1
  else:
    freq[rem]=1
  n=n//10
m=min(freq.values())
l_f={}
for key in freq:
  if freq[key]==m:
    l_f[key]=1
print( min(l_f.keys()))

# Input: n = 1553322
# Output: 1
