'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
 '''
piles = [3,6,7,11]
h = 8
ans=0
left=1
m=max(piles)
while left<=m:
  k=(left+m)//2
  time=0
  for i in range(len(piles)):
    a=piles[i]
    time+=(a+k-1)//k
    # if a%k==0:
    #   time+=a//k
    # else:
    #   time+=a//k+1
  if time<=h:
    ans=k
    m=k-1
  else:
    left=k+1
print(ans)

# Input: piles = [3,6,7,11], h = 8
# Output: 4
