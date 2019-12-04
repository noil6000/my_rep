path1 = input()
f1 = open(path1)
a1 = f1.read()
b1 = []
for i in a1.split("\n"):
    for n in i.split(" "):
        b1.append(float(n))

path2 = input()
f2 = open(path2)
a2 = f2.read()
b2 = []
for i in a2.split("\n"):
    for n in i.split(" "):
        b2.append(float(n))

n = 0
while n != len(b2):
    if b1[0] == b2[int(n)] and b1[1] == b2[int(n+1)]:
        print(0)
    elif b1[2] == b2[int(n)] and b1[3] == b2[int(n+1)]:
        print(0)
    elif b1[4] == b2[int(n)] and b1[5] == b2[int(n+1)]:
        print(0)
    elif b1[6] == b2[int(n)] and b1[7] == b2[int(n+1)]:
        print(0)
    
    elif b1[0] < b2[int(n)] and b1[1] == b2[int(n+1)] and b1[4] > b2[int(n+1)]:
        print(1)
    elif b1[2] < b2[int(n)] and b1[3] == b2[int(n+1)] and b1[6] > b2[int(n+1)]:
        print(1)
    elif b1[4] > b2[int(n)] and b1[5] == b2[int(n+1)] and b1[0] < b2[int(n+1)]:
        print(1)
    elif b1[6] > b2[int(n)] and b1[7] == b2[int(n+1)] and b1[2] < b2[int(n+1)]:
        print(1)

    elif b1[0] == b2[int(n)] and b1[1] < b2[int(n+1)] and b1[3] > b2[int(n+1)]:
        print(1)
    elif b1[2] == b2[int(n)] and b1[3] > b2[int(n+1)] and b1[1] < b2[int(n+1)]:
        print(1)
    elif b1[4] == b2[int(n)] and b1[5] > b2[int(n+1)] and b1[7] < b2[int(n+1)]:
        print(1)
    elif b1[6] == b2[int(n)] and b1[7] < b2[int(n+1)] and b1[5] > b2[int(n+1)]:
        print(1)

    elif b1[0] < b2[int(n)] and b1[1] < b2[int(n+1)] and b1[4] > b2[int(n)] and b1[5] > b2[int(n+1)]:
        print(2)
    else:
        print(3)
    n+=2

f1.close
f2.close