'''You are given an integer array nums and an integer k.
Return an integer denoting the sum of all elements in nums whose frequency is divisible by k, or 0 if there are no such elements.
Note: An element is included in the sum exactly as many times as it appears in the array if its total frequency is divisible by k.
''' 
#nums = [1,2,3,4,5], k = 2
nums = [1,2,2,3,3,3,3,4]
k = 2
ans=0
visited=[]
for i in range(len(nums)):
    if nums[i] not in visited:
        count=0 
        for num in nums:
            if num==nums[i]:
                count+=1
        if count%k==0:
            ans+=nums[i]*count
        visited.append(nums[i])
print(ans)

#another code 
# nums = [1,2,2,3,3,3,3,4]
# k = 2
# ans=0
# for i in nums:
#     c=nums.count(i)
#     if c%k==0:
#         ans+=i
# print(ans)