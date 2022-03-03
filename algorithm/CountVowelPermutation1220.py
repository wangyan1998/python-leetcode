class CountVowelPermutation1220:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        mod = 1000000007
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % mod, (dp[0] + dp[2]) % mod, (dp[1] + dp[3]) % mod, dp[2], (dp[2] + dp[3]) % mod)
        return sum(dp) % mod
