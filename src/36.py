import lib

s = 0
for x in range(1, 1000000):
    if lib.isPalindrome(x) and lib.isPalindrome(int('{0:b}'.format(x))):
        s += x
print(s)
