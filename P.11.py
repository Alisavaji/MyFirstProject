n = int(input("enter number of input"))
x = []
for i in range(n):
    z = input("enter number")
    x.append(int(float(z)))
p = []
N = []
for j in x:
    if j>=0:
        p.append(j)
    else:
        N.append(j)
print(p,N)
print(len(N))
