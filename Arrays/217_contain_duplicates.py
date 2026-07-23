'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''
nums=[1,2,3,1]
seen=[]
flag=False
for num in nums:
    if num in seen:
        flag=True
        break
    seen.append(num)
if flag:
    print("True")
else:
    print("False")
    
#another logic
nums=[1,2,3,4]
flag=False
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            flag=True
            break
if flag:
    print("True")
else:
    print("False")
        
# Input: nums = [1,2,3,1]
# Output: true


        
