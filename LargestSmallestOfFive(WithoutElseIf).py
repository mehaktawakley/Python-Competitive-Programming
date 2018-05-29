#WAP to print the largest and smallest no among given five numbers(take input from user...do not use if else).

print("Enter any 5 numbers to find greatest and smallest amongst them:")
a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))
d = int(input("4th number: "))
e = int(input("5th number: "))

print("Greatest is ", max(a,b,c,d,e))
print("Smallest is ", min(a,b,c,d,e))
