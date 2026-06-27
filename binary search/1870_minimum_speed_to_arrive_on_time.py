'''You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
Each train can only depart at an integer hour, so you may need to wait in between each train ride.
For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
'''
dist = [1,3,2]
hour = 6
n=len(dist)
if hours<n-1:
  return -1
left=1
right=10**7
ans=-1
while left<=right:
  k=(left+right)//k
  time=0
  for i in range(n-1):
    a=dist[i]
    if a%k==0:
      time+=a//k
    else:
      time+=(a//k)+1
  i=dist[-1]
  time+= i/k
  if time<=hours:
    ans=k
    right=k-1
  else:
    left=k+1
print(ans)
    
      
