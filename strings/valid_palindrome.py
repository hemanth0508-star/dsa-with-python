s="A man, a plan, a canal: Panama"

res=[i.lower() for i in s if i.isalnum()]
rev=res[::-1]
if rev==res:
    print("given string is a valid palindrome")
else:
    print("given string is not a valid palindrome")