lim = 100
ran = range(1, lim + 1)
xsqrf = sum(map(lambda x: x, ran))**2
xaddf = sum(map(lambda x: x**2, ran))
print(xsqrf - xaddf)
