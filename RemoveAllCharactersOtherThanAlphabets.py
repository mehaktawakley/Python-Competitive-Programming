"""
Given a string consisting of alphabets and others characters, the task is to remove all the characters other than alphabets and
print the string so formed.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case contains a string S.

Output:
For each test case, print the remaining string in new line, If no character remains in the string print "-1".

Constraints:
1<=T<=100
1<=|string length|<=105

Example:
Input:
2
$Gee*k;s..fo, r'Ge^eks?
P&ra+$BHa;;t*ku, ma$r@@s#in}gh
Output:
GeeksforGeeks
PraBHatkumarsingh
"""

count = int(input()) #Number of test cases

while(count>0):
    str1 = list(map(str,input())) #Taking input 
    str2 = ''
    for i in str1:
        if ((i>='a' and i<='z') or (i>='A' and i<='Z')): #Checking for Alphabets
            str2+=i

    if(len(str2)==0): #Checking if there are any characters in string
        print("-1")
    else:
        print(str2)

    count-=1
