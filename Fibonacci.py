#WAP to print the fibonacci series.

num = int(input("Fibonacci Series \nEnter Number of Desired Range:"))

a = 0
b = 1
c = 0
i = 0

if num==1:
    print(a)
elif num==2:
    print(a,b)

else:
    print(a)
    print(b)
    while i<num-2:
        c = a+b
        print(c)
        a = b
        b = c
        i = i+1
