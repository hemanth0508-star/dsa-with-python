'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
'''

nums=[1,2,3,4,2,5,7,8,2,3,6]

nums.sort()
print(max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3]))