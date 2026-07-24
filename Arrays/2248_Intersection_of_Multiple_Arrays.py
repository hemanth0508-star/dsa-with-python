'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
'''
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

ans=[]

for i in range(len(nums[0])):
    x=nums[0][i]
    count=1
    for j in range(1,len(nums)):
        flag=False
        for k in range(len(nums[j])):
            if nums[j][k]==x:
                flag=True
                break
        if flag:
            count+=1
    if count==len(nums) and nums[0][i] not in ans:
        ans.append(nums[0][i])
print(sorted(ans))
'''
#another code
ans=set(nums[0])
for i in range(1,len(nums)):
    ans=ans.intersection(nums[i])
sorted(list(ans))
'''

#Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
#Output: [3,4]      
