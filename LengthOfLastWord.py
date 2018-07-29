"""Given a string s consisting of upper/lower-case alphabets and empty space characters ‘ ‘, return length of the last word in the string. If the last word does not exist, return 0.

Note: The string can end with empty spaces also.

Input:
First line consists of T test cases. The only line of every test case consists of String S.

Output:
Single line output, Print the length of last word of string.

Constraints:
1<=T<=100
1<=|String length|<=100

Example:
Input:
2
Geeks for Geeks
Start Coding Here
Output:
5
4
"""

count = int(input())

while count>0:
    print(len((input().split())[-1]))
    
    count-=1
