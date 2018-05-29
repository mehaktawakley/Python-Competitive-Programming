#WAP to print the reverse of the no entered by the user(use logic).

num = int(input("Find Reverse of a Number \nEnter a number:"))
num1 = num
rev = 0

while(num>0):
    rem = num%10
    rev = rem + (rev*10)
    num = num//10

print("Reverse of ", num1, "is ", rev)
