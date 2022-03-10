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

## 算法分析2-7

我们可以发现，$n_1,n_2,\dots,n_d$ 恰好是函数 $P(x)$ 的 $d$ 个零点，于是有
$$
P(x)= \prod_{i=1}^{d}\left(x-n_i\right) =\prod_{i=1}^{\left\lfloor\frac{d}{2}\right\rfloor}\left(x-n_i\right) \prod_{i=\left\lfloor\frac{d}{2}\right\rfloor+1}^{d}\left(x-n_i\right)
$$
由第二个等号可知，$P(x)$ 可以分解为两个多项式的乘积，于是有递归式
$$
T\left(d\right)=
\begin{cases}
O(1)& \text{, d=1}\\
2T(\frac{d}{2})+O(d \log{d})& \text{, d>1}
\end{cases}
$$
解得 $T(d)=O(d\log^2{d})$

## 算法分析2-15

在总数 $n$ 为奇数位选手时，每一轮必定有一位选手轮空。只需把“轮空”也视为一位选手，转换为偶数位选手的算法即可。

在 $n/2$ 为奇数时，首先添加轮空，按照偶数位选手方法生成，例如当 $n/2=3$ 时，如下生成：
$$
\begin{matrix}  
1&2&3&4\\
2&1&4&3\\
3&4&1&2\\
4&3&2&1\\
\end{matrix}
$$
将多余生成的一列删去，轮空的置0，如下：
$$
\begin{matrix}  
1&2&3\\
2&1&0\\
3&0&1\\
0&3&2\\
\end{matrix}
$$
在合并时进行进一步处理，来看 $n=6$ 的情况，在 $n=3$ 的基础上，把天数依次扩张，轮空的0，用 $+3$ 号成员代替：
$$
\begin{matrix}  
1&2&3&4&5&6\\
2&1&6&5&4&3\\
3&0&1&\\
0&3&2\\
\end{matrix}
$$
扩张完毕后：
$$
\begin{matrix}  
1&2&3&4&5&6\\
2&1&6&5&4&3\\
3&5&1&6&2&4\\
4&3&2&1&6&5\\
\end{matrix}
$$
然后再进行纵向扩张，直到扩张完毕：
$$
\begin{matrix}  
2& 1& 6& 5& 4& 3\\
3& 5& 1& 6& 2& 4\\
4& 3& 2& 1& 6& 5\\
5& 6& 4& 3& 1& 2\\
6& 4& 5& 2& 3& 1\\
\end{matrix}
$$

## 算法实现2-6

```python
from math import factorial

def count(arr,n):
    """count the rank of the arrangement

    Args:
        arr (list): the arrangement list
        n (int): length

    Returns:
        int: the rank of the arrangement
    """    
    position=sorted(arr).index(arr[0])
    # if arr[0] is the k-th number, it has (k-1)*(n-1)! arrangements
    if(n==1):
        return (position)*factorial(n-1)
    return (position)*factorial(n-1)+count(arr[1:],n-1)
    
def next(arr,length):
    """calculate the next arrangement

    Args:
        arr (list): the arrangement list
        length (int): default 2
    """    
    # start from the last two numbers, if the former is smaller than the latter, it can be swapped
    # 1 2 3 4 -> 1 2 4 3
    if(length==2 and arr[-1]>arr[-2]):
        arr[-1],arr[-2]=arr[-2],arr[-1]
        return
    
    # else it has a carry, 2+1=3, and which behind it are the smallest numbers
    # 2 4 3 1 -> 3 1 2 4
    firstNum=arr[-length]
    minNum=arr[-length+1]
    
    if(max(arr[len(arr)-length:]) != firstNum):
        for num in arr[len(arr)-length:]:
            if(num<minNum and num>firstNum):
                minNum=num
                
        minPos=arr.index(minNum)
        arr[-length]=minNum
        # swap the smallest but bigger than the first number
        arr[minPos]=firstNum 
        
        arr[-length+1:]=sorted(arr[-length+1:]) # sort the numbers behind
        return
    
    next(arr,length+1)
    return

# read file
fin=open("input.txt","r")
content=fin.readlines()
n=int(content[0])
arrangement=list(map(int,content[1].split(',')))
fin.close()

# write file
fout=open("output.txt","w")
fout.write(str(count(arrangement,n))+'\n')
next(arrangement,2)
fout.write(str(arrangement))
fout.close()
```

输入输出：

| 输入 input.txt               | 输出 output.txt                             |
| ---------------------------- | ------------------------------------------- |
| 3<br/>2,1,3                  | 2<br/>[2, 3, 1]                             |
| 8<br/>2,6,4,5,8,1,7,3        | 8227<br/>[2, 6, 4, 5, 8, 3, 1, 7]           |
| 8<br/>4,5,6,8,1,2,3,9        | 17712<br/>[4, 5, 6, 8, 1, 2, 9, 3]          |
| 10<br/>4,5,6,15,12,3,9,8,7,1 | 821447<br/>[4, 5, 6, 15, 12, 7, 1, 3, 8, 9] |

