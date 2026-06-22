'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''
s = "  hello world  "
st=0
end=len(s)-1
while s[st]==" ":
    st+=1
while s[end]==" ":
    end-=1
    
word=''
ans=''
for ch in s[st:end+1]:
    if ch==' ':
        if word:
            ans=" "+word+ans
            word=""
    else:
        word+=ch
ans=" "+word+ans

print(ans.strip())
    