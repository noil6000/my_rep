import json
path = input()
f = open(path)
a = f.read()
b = []
for i in a.split("\n"):
    b.append(i.replace(":", "."))
b.sort()
c = ["tc", "te","userId", "condition"]
d = {}
l = []
n = 0
m = 1
for i in b:
    for k in i.split(' '):
        if m % 2 != 0:
            n+=1
            d["clientId"] = n
            d["tc"] = float(k)
            m+=1
        else:
            d["te"] = float(k)
            l.append(str(d))
            m+=1
d.clear()
n = 0
m = 0
j = 0
maxm = 0
sumd = {}
timer = 8.00
mint = 100
maxt = 0
while timer != 20.00:
    for i in l:
        d = json.loads(i.replace("'", '"'))
        if d["tc"] == timer:
            n+=1
            if n > m:
                m = n
    for i in l:
        d = json.loads(i.replace("'", '"'))
        if d["te"] == timer:
            n-=1
            if maxm <= m:
                j+=1
                if d["tc"] < mint:
                    mint = d["tc"]
                maxm = m
                maxt = d["te"]
                sumd["tc%s"%j] = str(mint)
                sumd["te%s"%j] = str(maxt)
                mint = 100
                maxt = 0
                m = 0
            

    timer += 0.01
    timer = round(timer, 2)
    if timer == 8.60:
        timer = 9.00
    elif timer == 9.60:
        timer = 10.00
    elif timer == 10.60:
        timer = 11.00
    elif timer == 11.60:
        timer = 12.00
    elif timer == 12.60:
        timer = 13.00
    elif timer == 13.60:
        timer = 14.00
    elif timer == 14.60:
        timer = 15.00
    elif timer == 15.60:
        timer = 16.00
    elif timer == 16.60:
        timer = 17.00
    elif timer == 17.60:
        timer = 18.00
    elif timer == 18.60:
        timer = 19.00
    elif timer == 19.60:
        timer = 20.00

flist = []
n = 1
for i in sumd:
    x = ('%.2f' % float(sumd[i]))
    if n % 2 != 0:
        print (x.replace(".", ":"), end = " ")
        n+=1
    else:
        print (x.replace(".", ":"))
        n+=1

f.close()