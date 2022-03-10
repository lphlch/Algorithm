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