"""
Given a single integer N, your task is to find the sum of the square of first N odd natural Numbers.

Examples:

Input : 3
Output : 35 
12 + 32 + 52 = 35

Input : 8
Output : 680
12 + 32 + 52 + 72 + 92 + 112 + 132 + 152 
Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The only line of each test case contains an integer N.

Output:
For each test case output the required anser on a new line.

Constraints:
1<=T<=100
0<=N<=104

Example:
Input:
3
2
5
9
Output:

10
165
969S
"""

t = int(input())

while (t>0):
    n = int(input())
    print((4*(n**3)-n)//3)
    t-=1
