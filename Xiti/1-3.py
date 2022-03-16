class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A==1:
            return B
        
        if A%2==0:
            return self.multiply(A>>1,B)<<1
        else:
            return B+(self.multiply(A>>1,B)<<1)