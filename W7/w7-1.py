class Solution:
    dp = []

    def numTrees(self, n: int) -> int:
        # init dp
        if self.dp == []:
            self.dp = [0]*(n+1)

        # base case
        if n == 1 or n == 0:
            self.dp[1] = 1
            return 1
        if n == 2:
            self.dp[2] = 2
            return 2

        # dynamic programming
        if self.dp[n] != 0:
            return self.dp[n]

        # recursive
        sum = 0
        for i in range(1, n+1):
            sum += self.numTrees(i-1)*self.numTrees(n-i)
        self.dp[n] = sum

        return sum
