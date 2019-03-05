ps = 0
tris = 0
for p in range(30, 1000, 30):
    tri = []
    print(p)
    for a in range(1, p / 2):
        for b in range(a, p / 2):
            for c in range(b, p / 2):
                if a + b + c == p:
                    if a**2 + b**2 == c**2:
                        tri.append({a, b, c})
    if len(tri) > tris:
        ps = p
        tris = len(tri)
print(ps)
