"""
Given a list of characters, merge all of them into a string.

Input:
First line of the input contains an integer T, denoting the number of testcases. Then T test case follows. Each testcase contains two lines:-
The number of characters in the array N.
The array of characters separated by space

Output:
For each testcase, print the character array converted into a string.

Constraints:
1<=T<=100
10<=N<=100


Example:

Input:
2
13
g e e k s f o r g e e k s
11
p r o g r a m m i n g

Output:
geeksforgeeks
programming
"""

count = int(input())

while count>0:
    input()
    print("".join(input().split(" ")))
    count-=1
