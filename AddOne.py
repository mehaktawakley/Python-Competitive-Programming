"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). The digits are stored such that the most significant digit is at the head of the list.

Example:
If the array has [4, 5, 6]
the resultant array should be [4, 5, 7]
as 456 + 1 = 457.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the space separated resultant array in a separate line for each case.

Constraints: 
1 ≤ T ≤ 30
1 ≤ N ≤ 1000
0 ≤ A[i] ≤ 9

Example: 
Input:
2
4
5 6 7 8
3
9 9 9
Output:
5 6 7 9
1 0 0 0 
"""

count = int(input())

while count>0:
    int(input())
    n = list(map(str,input().split()))
    n1 = list(str(int("".join(n))+1))
    while len(n) > len(n1):
        n1.insert(0,'0')
    print(*n1)
    count-=1
