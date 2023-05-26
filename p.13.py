n= int(input("enter a number:"))
for i in range(n+1):
    if (n-i)==n:
        x="*"*0
    else:
        x="*"*1
    print(f'{" "*(n-i)+"*"+" "*(2*i-1)+x}') 
for j in range(n):
    if n==j+1:
        y="*"*0
    else:
        y="*"*1
    print(f'{" "*(j+1)+"*"+" "*((2*n-4)-(2*j-1))+y}')
    
