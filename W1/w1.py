while True:
    n=int(input("Enter a number: "))
    if n<0:
        is_negative=True
        n=-n
    else:
        is_negative=False
    left=1
    right=n

    while True:
        result=int((left+right)/2)  # 二分法
        if result*result<=n<(result+1)*(result+1):
            break
        elif result*result>n:
            right=result
        else:
            left=result
    
    if is_negative:
        print("The sqrt is: ",result,"i")
    else:
        print("The sqrt is: ",result)
