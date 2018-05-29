#WAP to perform linear search

n = int(input("Enter number of terms you want to enter:"))

arr = []

for i in range(0,n):
    num = int(input("Enter element :"))
    arr.append(num)

search = int(input("Enter the number you want to find: "))

for i in range(0,n):
    if arr[i]==search:
        print("Element Found At Position:" , i+1)
        break
