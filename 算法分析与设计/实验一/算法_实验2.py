def lcs(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[n][m]

    def backtrack(i, j):
        if i == 0 or j == 0:
            return set([""])
        elif X[i - 1] == Y[j - 1]:
            return {sub + X[i - 1] for sub in backtrack(i - 1, j - 1)}
        else:
            results = set()
            if dp[i - 1][j] >= dp[i][j - 1]:
                results.update(backtrack(i - 1, j))
            if dp[i][j - 1] >= dp[i - 1][j]:
                results.update(backtrack(i, j - 1))
            return results

    all_lcs = list(backtrack(n, m))
    print(lcs_length)
    for seq in sorted(all_lcs):
        print(seq)


input_X = input('输入第一个字符串：')
input_Y = input('输入第二个字符串：')
lcs(input_X, input_Y)
