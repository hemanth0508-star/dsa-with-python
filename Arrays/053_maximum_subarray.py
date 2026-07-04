'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
nums=[-2,1,-3,4,-1,2,1,-5,4]
sum=nums[0]
max=nums[0]
start=0
end=0
temp=0
for i in range(1,len(nums)):
    if nums[i]>sum+nums[i]:
        sum=nums[i]
        temp=i
    else:
        sum=nums[i]+sum
    if max<sum:
        max=sum
        start=temp
        end=i
print(max,nums[start:end+1])

#here start and end  used to return the values of maximum subarray
