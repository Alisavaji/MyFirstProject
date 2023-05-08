n = int(input("enter number of input"))
x = []
for i in range(n):
    z = input("enter number")
    x.append(int(float(z)))
k = []
for j in x:
    if j>=0:
        k.append(True)
    else:
        k.append(False)
d = {1:"is"}
if all (k):
    print ("all numbers are positive")
else:
    f = k.count(False)
    if f == len(k):
        print("all numbers are negetive")
    else:
        print("{:} number{:} negetive".format(f,d.get(f, "s are")))
        
