# 算法第2次作业

2052336 吕品灏

## 青蛙跳台阶

```python
class Solution:
    def numWays(self, n: int) -> int:
        if(n == 0):
            return 1
        count=[0]*(n+1)     # init count list
        count[0]=1
        count[1]=1
        for i in range(2,n+1):
            count[i]=(count[i-1]+count[i-2]) % 1000000007
        return count[n]
    
    # time out of limits
    '''
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        sum = self.numWays(n-1)+self.numWays(n-2)
        return sum
    '''
```

![w2-1](F:\CodeProject\Algorithm\img\w2-1.jpeg)

## 至少有 K 个重复字符的最长子串

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if(len(s) < k):
            return 0

        for ch in set(s):   # set means no duplicate
            if(s.count(ch) < k):
                # split string by ch, and ch will not appear in set
                subStrings = s.split(ch)
                maxLen = 0
                for subString in subStrings:
                   maxLen = max(self.longestSubstring(subString, k), maxLen)
                return maxLen
        return len(s)
```

![w2-2](F:\CodeProject\Algorithm\img\w2-2.jpeg)

## 最小的k个数

```python
class Solution:
    def partition(self,arr,p,r,k):
        #print('partition',p,r,k)
        i=p+1
        j=r
        x=k
        while True:
            while arr[i]<x and i<r:
                #print('i',i)
                i+=1
            while arr[j]>=x and j>p:
                #print('j',j)
                j-=1
            if i>=j:
                break
            arr[i],arr[j]=arr[j],arr[i]
        pos=arr.index(x)
        arr[pos]=arr[j]
        arr[j]=x
        return j
    
    
    def select(self,arr,p,r,k):
        #print('selecting',p,r,k)
        if(r-p<75):
            arr[p:r+1]=sorted(arr[p:r+1])
            return arr[p+k-1]
        
        for i in range(0,int((r-p-4)/5+1)):
            arr[p+5*i:p+5*i+4+1]=sorted(arr[p+5*i:p+5*i+4+1])    # sort 5 elements, for get the median
            arr[p+i],arr[p+5*i+2]=arr[p+5*i+2],arr[p+i]   # swap the median to the first position, for better getting the median of medians
            x=self.select(arr,p,int(p+(r-p-4)/5),int((r-p-4)/10))
            i=self.partition(arr,p,r,x)    # partition the array
            j=i-p+1
            if(k<=j):
                return self.select(arr,p,i,k)
            else:
                return self.select(arr,i+1,r,k-j)
            
    def getLeastNumbers(self, arr, k: int):
        kthNum=self.select(arr,0,len(arr)-1,k)
        nums=[num for num in arr if num<=kthNum]
        nums.sort()
        return nums[:k]
```

![w2-3](F:\CodeProject\Algorithm\img\w2-3.jpeg)

## 