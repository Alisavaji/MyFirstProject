n= int(input("enter a number:"))
for i in range(n+1):
    print(f'{" "*(n-i)+"*"+" "*(2*i-1)+"*"}') 
for j in range(n):
    print(f'{" "*(j+1)+"*"+" "*((2*n-4)-(2*j-1))+"*"}')
