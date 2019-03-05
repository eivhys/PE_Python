import lib

result = 0
i = 143
searching = True

while (searching):
    i = i + 1
    result = i * (2 * i - 1)

    if (lib.isPentagonal(result)):
        searching = False
print(result)
