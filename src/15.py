import lib

x = 20
y = 20

print(lib.factorial(x + y) / (lib.factorial(x) * lib.factorial((x + y) - x)))
