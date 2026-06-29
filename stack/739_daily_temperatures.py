'''Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
temperatures = [73,74,75,71,69,72,76,73]
n=len(temperatures)
ans=[0]*n
stack=[]
for i in range(n):
    while stack and temperatures[i]>temperatures[stack[-1]]:
        ind=stack.pop()
        ans[ind]=i-ind
    stack.append(i)
print(ans)













#brut force for this prblm
ans=[]
for i in range(len(temperatures)):
    d=0
    for j in range(i+1,len(temperatures)):
        if temperatures[j]>temperatures[i]:
            d=j-i
            break
    ans.append(d)
print(ans)