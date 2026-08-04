class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        prime=[True]*n
        prime[0],prime[1]=False,False
        p=2
        ans=0
        while p<n:
            if prime[p]==True:
                ans+=1
                for i in range(p*p,n,p):
                    prime[i]=False
            p+=1
        return ans

#Input: n = 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
