"""
Given an integer array, for each element in the array check whether there exist a smaller element on the next immediate position of the array. If it exist print the smaller element. If there is no smaller element on the immediate next to the element then print -1.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains an integer N, where N is the size of array.
The second line of each test case contains N integers sperated with a space which is input for the array arr[ ]

Output:
For each test case, print in a newline the next immediate smaller elements for each element in the array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ arr[i] ≤ 1000

Example:
Input
2
5
4 2 1 5 3
6
5 6 2 3 1 7

Output
2 1 -1 3 -1
-1 2 -1 1 -1 -1
"""

count = int(input())

while count>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(0,n-1):
        if ((a[i+1])<a[i]):
            b.append(a[i+1])
        else:
            b.append(-1)
    b.append(-1)
    print(*b)
    count-=1
