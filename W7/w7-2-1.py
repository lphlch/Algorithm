def plan(n, a, b):

    maxSingle = max(max(a), max(b))
    maxTime = maxSingle*n
    dp = [[[0]*(n+1) for i in range(maxTime+1)] for j in range(maxTime+1)]

    # base case
    for i in range(maxTime+1):
        for j in range(maxTime+1):
            dp[i][j][0] = 1

    # dynamic programming
    for k in range(1, n+1):  # for k works
        for i in range(maxTime+1):
            for j in range(maxTime+1):
                # ! notice that, in python, negative can be the index without error
                if i-a[k-1] >= 0 and j-b[k-1] >= 0:
                    dp[i][j][k] = dp[i-a[k-1]][j][k-1] or dp[i][j-b[k-1]][k-1]

                else:
                    if i-a[k-1] >= 0:   # if the k th work can be done by a machine within time i
                        dp[i][j][k] = dp[i-a[k-1]][j][k-1]
                    if j-b[k-1] >= 0:   # if the k th work can be done by b machine within time j
                        dp[i][j][k] = dp[i][j-b[k-1]][k-1]

    # get min time
    time = maxTime
    for i in range(maxTime+1):
        for j in range(maxTime+1):
            if dp[i][j][n] == 1:
                time = min(time, max(i, j))

    return time


# read file
fin = open("input.txt", "r")
content = fin.readlines()
n = int(content[0])
a, b = list(map(int, content[1].split())), list(map(int, content[2].split()))
fin.close()

time = plan(n, a, b)

# write file
fout = open("output.txt", "w")
fout.write(str(time))
fout.close()

time = plan(6, [2, 5, 7, 10, 5, 2], [3, 8, 4, 11, 3, 4])
print(time)
