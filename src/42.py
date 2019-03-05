import lib

with open('../misc/42.txt', 'r') as problem:
    data = problem.read().replace('\n', '').replace('"', '')

names = sorted(data.split(","))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sums = []
s = 0
for name in names:
    namesum = 0
    for letter in name:
        for x in xrange(0, len(alphabet)):
            if letter == alphabet[x]:
                namesum += x + 1
    print(name, namesum)
    t = 0
    tri = 0
    while tri < namesum:
        t += 1
        tri = lib.triangle(t)
    if tri == namesum:
        sums.append(namesum)
        s += 1

print(len(sums))
