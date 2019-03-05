terms = []
lim = 100
for x in range(2, lim+1):
    for y in range(2, lim+1):
        terms.append(x**y)
print(len(set(sorted(terms))))
