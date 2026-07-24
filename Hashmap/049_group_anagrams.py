'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
strs=["eat","tea","tan","ate","nat","bat"]

hash_map={}
for string in strs:
    sorted_string=''.join(sorted(string))
    if sorted_string in hash_map:
        hash_map[sorted_string].append(string)
    else:
        hash_map[sorted_string]=[string]
print(hash_map)
print(hash_map.values())        

# #this is done by hashmap data structure
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
