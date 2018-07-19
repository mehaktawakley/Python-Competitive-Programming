"""
Given a string, remove the vowels from the string and print the string without vowels.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of a string s. 

Output:
Print the required output.

Constraints: 
1<=T<=100
1<=|Length of string|<=1000

Example:
Input:
2
welcome to geeksforgeeks
what is your name ?

Output:
wlcm t gksfrgks
wht s yr nm ?
"""

count = int(input())

while(count>0):
    string = str(input())
    string1 = ""
    for x in string:
        if x not in "aeiou":
            string1 = string1 + x

    print(string1)

    count= count-1
