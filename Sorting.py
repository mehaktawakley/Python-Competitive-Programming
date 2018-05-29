# WAP to sort an array using 1 line code.

n = int(input("Enter number of terms you want to enter:"))

arr = []

for i in range(0,n):
    num = int(input("Enter element :"))
    arr.append(num)

print("You have entered following elements:")
for i in arr:
    print(i)

arr.sort()

print("After Sorting")

for i in arr:
    print(i)
