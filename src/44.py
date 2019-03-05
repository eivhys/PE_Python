import lib

searching = True
i = 1

while (searching):
    i = i + 1
    n = i * (3 * i - 1) / 2
    for j in range(i-1, 0, -1):
        m = j * (3 * j - 1) / 2
        if lib.isPentagonal(n - m) and lib.isPentagonal(m + n):
            result = n-m
            searching = False
            print(result)
            break
