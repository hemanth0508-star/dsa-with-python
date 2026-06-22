'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string
'''
strs = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(strs[0])):
    ch = strs[0][i]

    for s in strs:
        if i == len(s) or s[i] != ch:
            print(prefix)
            exit()

    prefix = prefix + ch

print(prefix)