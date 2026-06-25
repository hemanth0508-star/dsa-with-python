'''
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
'''
nums = [1,2,2,3,1,4]

freq={}
for i in range(len(nums)):
  freq[nums[i]]=freq.get(nums[i],0)+1
max=0
for key in freq:
  if freq[key]>max:
    max=freq[key]
ans=0
for key in freq:
  if freq[key]==max:
    ans+=freq[key]
print( ans)

