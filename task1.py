import math


def per(N, key=lambda x:x):
    k = (len(N)-1) * 0.9
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def med(N, key=lambda x:x):
    k = (len(N)-1) * 0.5
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def mid(N):
    s = (sum(N)/len(N))
    return s

path = input()
f = open(path)
a = f.read()
b = []
for i in a.split("\n"):
    b.append(int(i))
b.sort()

c = (per(b))
print ('%.2f' % c)

c = (med(b))
print ('%.2f' % c)

c = (max(b))
print ('%.2f' % c)

c = (min(b))
print ('%.2f' % c)

c = (mid(b))
print ('%.2f' % c)

f.close