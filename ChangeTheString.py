"""
Given a string S, the task is to change the string according to the condition; If the first letter in a string is capital letter then change the full string to capital letters, else change the full string to small letters.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string S.

Output:
For each test case, print the changed string in a new line.

Constraints:
1<=T<=200
1<=|string length|<=104

Example:
Input:
2
geEkS
FoR
Output:
geeks
FOR
"""
count = int(input())
while count>0:
    string = input()
    print(string.upper() if string[0].isupper() else string.lower())
    count-=1
