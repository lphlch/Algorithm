def hanoi(level, source, dest, temp, fout):
    """solve hanoi problem with color check, and print moving steps

    Args:
        level (int): level of hanoi tower
        source (string): source tower name
        dest (string): destination tower name
        temp (string): middle tower name
        fout (file handle): file handle of output file
    """    
    if level == 1:
        fout.write("1 "+source+' '+dest+"\n")
    else:
        hanoi(level-1, source, temp, dest, fout)

        #move
        if(source == "A"):
            arrSource = a
        elif(source == "B"):
            arrSource = b
        else:
            arrSource = c
        if(dest == "A"):
            arrDest=a
        elif(dest=="B"):
            arrDest=b
        else:
            arrDest=c
        if(len(arrDest)!=0 and (arrSource[-1]+arrDest[-1])%2 == 0 ):    # check if the last two disks are even or odd
            fout.write("ERROR!")
        else:
            arrDest.append(arrSource.pop())
            fout.write(str(level)+' '+source+' '+dest+"\n")

        hanoi(level-1, temp, dest, source, fout)


# read file
fin = open("input.txt", "r")
content = fin.readlines()
n = int(content[0])
fin.close()

global a, b, c
a = [x for x in range(1, n+1)]
b = []
c = []

# write file
fout = open("output.txt", "w")
hanoi(n, "A", "B", "C", fout)
fout.close()
