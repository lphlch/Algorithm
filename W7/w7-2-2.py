from cmath import inf

def getMaxCuboid(m, n, p):
    dp = [[[[[[0]*(p) for i in range(p)]
            for j in range(n)] for k in range(n)]
          for l in range(m)] for ll in range(m)]
    # dp index means top-left corner to bottom-right corner value means the data of sub-cuboid
    
    for mLen in range(1, m+1):
        for nLen in range(1, n+1):
            for pLen in range(1, p+1):  # for each length
                for mBase in range(m-mLen+1):
                    for nBase in range(n-nLen+1):
                        for pBase in range(p-pLen+1):   # for each base
                            # base case
                            if mLen == 1 and nLen == 1 and pLen == 1:
                                dp[mBase][mLen+mBase-1]\
                                [nBase][nLen+nBase-1]\
                                [pBase][pLen+pBase-1] = cuboid[mBase][nBase][pBase]
                                continue
                            
                            # dynamic programming
                            # extend in different direction once
                            if pLen == 1 and nLen != 1:
                                dp[mBase][mLen+mBase-1]\
                                [nBase][nLen+nBase-1]\
                                [pBase][pLen+pBase-1] = dp[mBase][mLen+mBase-1]\
                                [nBase][nLen+nBase-2]\
                                [pBase][pLen+pBase-1]+dp[mBase][mLen+mBase-1]\
                                [nLen+nBase-1][nLen+nBase-1]\
                                [pBase][pLen+pBase-1]
                                continue
                                
                            if pLen == 1 and mLen != 1:
                                dp[mBase][mLen+mBase-1]\
                                [nBase][nLen+nBase-1]\
                                [pBase][pLen+pBase-1] = dp[mBase][mLen+mBase-2]\
                                [nBase][nLen+nBase-1]\
                                [pBase][pLen+pBase-1]+dp[mLen+mBase-1][mLen+mBase-1]\
                                [nBase][nLen+nBase-1]\
                                [pBase][pLen+pBase-1]
                                continue

                            
                            dp[mBase][mLen+mBase-1]\
                            [nBase][nLen+nBase-1]\
                            [pBase][pLen+pBase-1] = dp[mBase][mLen+mBase-1]\
                            [nBase][nLen+nBase-1]\
                            [pBase][pLen+pBase-2]+dp[mBase][mLen+mBase-1]\
                            [nBase][nLen+nBase-1]\
                            [pLen+pBase-1][pLen+pBase-1]
                    
    # get max cuboid        
    maxNum=-inf
    for m1 in range(m):
        for m2 in range(m1,m):
            for n1 in range(n):
                for n2 in range(n1,n):
                    for p1 in range(p):
                        for p2 in range(p1,p):
                            maxNum=max(maxNum,dp[m1][m2][n1][n2][p1][p2])
                            #print("m %d to %d, n %d to %d, p %d to %d, value= %d" % (m1, m2, n1, n2, p1, p2,dp[m1][m2][n1][n2][p1][p2]))
                    
    return maxNum

# read file
fin = open("input.txt", "r")
content = fin.readlines()
m, n, p = list(map(int, content[0].split()))

global cuboid
cuboid = []
for i in range(m):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int, content[i*n+j+1].split())))
    cuboid.append(tmp)
fin.close()

result=getMaxCuboid(m, n, p)

# write file
fout = open("output.txt", "w")
fout.write(str(result))
fout.close()

print(result)

