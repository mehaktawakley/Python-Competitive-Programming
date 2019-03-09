"""
Write a program to reverse digits of a number N.

Input:
The first line of input contains an integer T, denoting the number of test cases. T testcases follow. Each test case contains an integer N.

Output:
For each test case, print the reverse digits of number N .

Constraints:
1 ≤ T ≤ 104
1 ≤ N ≤ 1015

Example:
Input:
2
200
122
Output:
2
221
"""

t = int(input())

while t>0:
    num = int(input())
    rev = 0
    
    while(num!=0):
        rev = num%10 + (rev*10)
        num = num//10
    print(rev)
    
    t-=1