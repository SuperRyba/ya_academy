import sys
data = list(map(str.strip, sys.stdin))
data = list(map(lambda x: x.lower(), data))
del data[0]
dop_spis = {}

for i in data:
    dop_i = []
    dop_i.extend(i)
    dop_i = sorted(str(dop_i))
    A = ''.join(dop_i)

    if A in dop_spis.keys():
        dop_spis[A] += f'{i} '
    else:
        dop_spis[A] = f'{i} '

del data
itog = [dop_spis[l].split() for l in dop_spis]
del dop_spis
itog.sort(key=lambda x: ''.join(x))
for p in itog:
    if len(p) != 1:
        print(' '.join(p))