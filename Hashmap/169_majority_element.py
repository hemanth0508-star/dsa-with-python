'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
nums = [2,2,1,1,1,2,2]
freq={}
for i in nums:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
m=max(freq.values())
for key in freq:
  if freq[key]==m:
    print(key)
    break
#this is sloved by the hashset
