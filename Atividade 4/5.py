memo = {}

def T(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = T(n - 1) + 2 * T(n - 2)

    return memo[n]

sequencia = lambda n: T(n)

for i in range(10):
    print(f"T({i}) = {sequencia(i)}")