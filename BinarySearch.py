#WAP to perform binary search.

n = int(input("Enter the number of elements you want to enter: "))

arr = []

for i in range(0,n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter the element you want to search: "))

start = 0
end = n
mid = (start+end)//2
found = False

while(start<=end and not found):
    mid = (start+end)//2

    if arr[mid] == search :
        print("Element found at ",mid+1," position ")
        found = True

    else:
        if(search<arr[mid]):
            start = 0
            end = mid

        elif(search>arr[mid]):
            start = mid
            end = n


