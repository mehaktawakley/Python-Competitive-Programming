"""
Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a string S.
Output:
For each test case, print four lines. In the first line print the count of upper case letters, in the second line print the count of lower case letters, in the third line print the count of numbers and in the fourth line print the count of special characters present in the string S.

Note: The strings doesnot contains whitespaces.

Constraints:
1<=T<=100
1<=length(S)<=100000

Example:
Input:
2
#GeeKs01fOr@gEEks07
*GeEkS4GeEkS*
Output:
5
8
4
2
6
4
1
2
"""

count = int(input())

while count>0:
    s = input()
    uc, lc, no, sc = 0,0,0,0
    for i in s:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            no+=1
        else:
            sc+=1
    print(uc)
    print(lc)
    print(no)
    print(sc)
    count-=1
