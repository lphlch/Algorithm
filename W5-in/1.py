class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        memo=[0,1,-1]
        i=0
        while i<n:
            i+=1
            memo[2]=memo[0]+memo[1]
            memo[0]=memo[1]
            memo[1]=memo[2]
        
        return memo[0]
