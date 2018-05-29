#WAP to print the largest no among given three numbers(take input from user...use if else).

print("Find Largest Of Entered Three Numbers")
print("Enter any three numbers:")
a = int(input())
b = int(input())
c = int(input())
print("Entered Numbers Are:: \nA = ",a,"\nB = ",b,"\nC = ",c)
if a>b:
    if a>c:
        print(a, " is Greatest")
    elif c>a:
        print(c, " is Greatest")
elif b>c:
    print(b, " is Greatest")
else:
    print(c, " is Greatest")
