"""
Given an unsorted array of N integers which can contain integers from 1 to N. Some elements can be repeated multiple times and some other elements can be absent from the array. Count frequency of all elements from 1 to N.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each test case output N space-separated integers denoting the frequency of each element from 1 to N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
5
2 3 2 3 5
4
3 3 3 3

Output:
0 2 2 0 1
0 0 4 0
"""
count = int(input())

while count>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*n
    for i in range(1,n+1):
        if i in a:
            b[i-1] = a.count(i)
    print(*b)
    count-=1
