'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
nums = [2,2,1,1,1,2,2]
n=len(nums)
for i in range(n):
    count=1
    for j in range(n):
        if i!=j and nums[i]==nums[j]:
            count+=1
    if count>n//2:
        print(nums[i])
        break