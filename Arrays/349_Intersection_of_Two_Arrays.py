'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''
#nums1 = [4,9,5]
#nums2 = [9,4,9,8,4]
nums1 = [1,2,2,1]
nums2 = [2,2]
list=[]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]==nums2[j] and nums1[i] not in list:
            list.append(nums1[i])
            break
print(list)

'''
#another code
n1=set(nums1)
n2=set(nums2)
seen=[]
for i in n1:
    if i in n2:
        seen.append(i)
        
# '''
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
