"""
Given an array, swap kth element from beginning with kth element from end.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and k,N is the size of array and kth number.
The second line of each test case contains N input C[i].

Output:
Print the modified array.

Constraints:
1 ≤ T ≤ 100
1 ≤ K ≤ N ≤ 500
1 ≤ C[i] ≤ 1000

Example:
Input
1
8 3
1 2 3 4 5 6 7 8
Output
1 2 6 4 5 3 7 8
"""

count = int(input())

while count>0:
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b[a[1]-1],b[-a[1]] = b[-a[1]],b[a[1]-1]
    print(*b)
    count-=1
