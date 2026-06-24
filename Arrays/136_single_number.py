'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
nums = [4,1,2,1,2]

n=len(nums)
for i in range(n):
    flag=True
    for j in range(n):
        if i!=j and nums[i]==nums[j]:
            flag=False
            break
    if flag:
        print(nums[i])
        break