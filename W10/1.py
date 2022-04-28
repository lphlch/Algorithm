from functools import cmp_to_key

def strCmp(x,y):
    if x==y:
        return 0
    
    n=min(len(x),len(y))
    for i in range(n):
        if x[i]<y[i]:
            return 1
        if x[i]>y[i]:
            return -1
    
    if len(x)<len(y):
        return -1
    return 1

def getMaxNum(nums):
    n=len(nums)
    # convert to list of strings
    strNums=[]
    for num in nums:
        strNums.append(str(num))
    
    result=''
    strNums.sort(key=cmp_to_key(strCmp))    # use costumized compare function to sort strings
    for sortedStrNum in strNums:
        result+=sortedStrNum
    return int(result)


nums=input().split(',')
print(getMaxNum(nums))