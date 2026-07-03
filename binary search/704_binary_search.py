'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
'''
nums = [-1,0,3,5,9,12]
target = 9
left=0
right=len(nums)-1
while left<right:
  mid=(left+right)//k
  if nums[mid]==target:
    print(mid)
    break
  elif nums[mid]<target:
    left=mid+1
  else:
    right=mid-1
