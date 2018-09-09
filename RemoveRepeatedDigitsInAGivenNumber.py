"""
Given an integer N, remove consecutive repeated digits from it.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integer N.

Output:
Print the number after removing consecutive digits. Print the answer for each test case in a new line.


Constraints:
1<= T <=100
1<= N <=1018


Example:
Input:
1
12224

Output:
124
"""

t = int(input())

while(t>0):
    n = input()
    n1 = []
    n1.append(n[0])

    for i in n:
        if(n1[-1] != i):
            n1.append(i)
            
    print("".join(n1))
    t-=1