#WAP to perform bubble sort

n = int(input("Enter number of terms you want to enter:"))

arr = []

for i in range(0,n):
    num = int(input("Enter element :"))
    arr.append(num)

print("You have entered following elements:")
for i in arr:
    print(i)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("After Bubble Sorting:")
for i in arr:
    print(i)
