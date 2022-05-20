from cmath import sqrt


class Circle:

    def __init__(self,n,listOfR) -> None:
        self.minValue=float('inf')
        self.x=[0]*(n+1)
        self.r=[0]+listOfR
        self.n=n
        self.checked=[]

    def center(self, t: int):
        """calculate position of center of circle

        Args:
            t (int): number of circle
        Returns:
            float: position of the center of circle
        """      
        tmp = 0
        for j in range(1, t):
            valueX = self.x[j]+2*(sqrt(self.r[t]*self.r[j]).real)
            tmp=max(tmp,valueX)
            
        return tmp
    
    def compute(self):
        """computer length of current solution
        """        
        low=high=0
        for i in range(1,self.n+1):
            low=min(low,self.x[i]-self.r[i])
            high=max(high,self.x[i]+self.r[i])
        self.minValue=min(self.minValue,high-low)
        
    def backtrack(self,t:int):
        """backtrack to find the best solution

        Args:
            t (int): number of current circle
        """        
        if t>self.n:
            self.compute()
        else:
            for j in range(t,self.n+1):
                self.r[t],self.r[j]=self.r[j],self.r[t] # make new case
                
                centerX=self.center(t)
                
                if centerX+self.r[t]+self.r[1] < self.minValue and self.r[1:j+1] not in self.checked:
                    self.x[t]=centerX
                    print("curr:",self.r[1:j+1])
                    self.backtrack(t+1) # deeper case
                    self.checked.append(self.r[1:j+1])
                    self.checked.append(list(reversed(self.r[1:j+1])))
                    
                self.r[t],self.r[j]=self.r[j],self.r[t] # back
                
def circlePerm(n,listOfR):
    c=Circle(n,listOfR)
    c.backtrack(1)
    return c.minValue

circlePerm(7,[1,2,3,3,3,2,1])
            
