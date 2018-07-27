"""
Given an array with all elements greater than or equal to zero.Return the maximum product of two numbers possible.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, N is size of array.
The second line of each test case contains N input A[i].

Output:
Print the maximum product of two numbers possible.

Constraints:
1 ≤ T ≤ 20
2 ≤ N ≤ 50
0 ≤ A[i] ≤ 1000

Example:
Input
1
5
1 100 42 4 23

Output
4200
"""

count = int(input())

while count>0:
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    print (l[n-1]*l[n-2])
    count-=1
