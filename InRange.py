"""
You are given n inputs and two numbers x and y.
check whether all the given numbers lies in range of x and y. (x <= y).
If the condition is true print YES else print NO.

input Format:
First line contains N, X, Y seperated by space.
Next Line contains n integers.

SAMPLE INPUT 
5 1 5
1 2 3 4 5
SAMPLE OUTPUT 
YES
"""

n,x,y = map(int,input().strip().split(" "))
flag = True

arr = list(map(int,input().split()))

if (x>y):
    flag = False

else:
    for i in range(n):
        if (x<=arr[i] and y>=arr[i]):
            flag = True
        else:
            flag = False
            break

if (flag == False):
    print("NO")

else:
    print("YES")
