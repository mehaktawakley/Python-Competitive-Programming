#WAP to add the original and reverse of the same no then print the result.(take input from user).

num = int(input("Enter a number: "))
x = num
rev = 0

while(num>0):
    rem = num%10
    rev = (rev*10) + rem
    num = num//10

print("Result: " ,x+rev)
