import glob

def cash(l):
    i = 0
    n = 0
    m = 0
    while i != len(l):
        if l[int(i)] > m:
            m = l[int(i)]
            n = i+1
        i+=1
    d = dict([(n, m)])
    return d

path = input()
cl = glob.glob("%s/*.txt" % path)
cl.sort()
pl = []
for i in cl:
    f = open(i)
    a = f.read()
    b = []
    for i in a.split("\n"):
        for n in i.split(" "):
            b.append(float(n))
    pl.append(cash(b))

n = 0
m = 0
#k = 1
for i in pl:
    if i.get(max(i)) > n:
        n = i.get(max(i))
        m = i

for i in m:
    print (i)