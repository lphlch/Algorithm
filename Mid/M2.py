from cmath import sqrt


def museumGuardPatrol(points)->float:
    n=len(points)
    # count distance between two points
    distanceList=[[0]*n for _ in range(n)]
    for i,point1 in enumerate(points):
        for j,point2 in enumerate(points):
            distanceList[i][j]=(sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)).real
            
    # dynamic programming
    guards=[[[]*n for __ in range(n)]*n for _ in range(n)]
    dp = [[0] * n for _ in range(n)] # dp[i][j] is the minimum length between i and j
    for length in range(3, n + 1) :
        for i in range(0, n - length + 1) :
            j = i + length - 1
            dp[i][j] = 999999999999999
            for k in range(i + 1, j) :
                if dp[i][j] > dp[i][k] + dp[k][j] + distanceList[i][k] + distanceList[k][j]+distanceList[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j] + distanceList[i][k] + distanceList[k][j]+distanceList[i][j]
                    guards[i][j] = guards[i][k]+guards[k][j]+[[points[i],points[j],points[k]]]
                    

    return dp[0][n - 1],guards[0][n - 1]

print(museumGuardPatrol([[0,0],[sqrt(3).real,1],[-sqrt(3).real,-1]]))

