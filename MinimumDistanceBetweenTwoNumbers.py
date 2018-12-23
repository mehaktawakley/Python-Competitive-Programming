"""
You are given an array A, of N elements. You need to find minimum distance between given two integers x and y.

Input Format:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. The first line of each test case contains an integer N denoting size array. Then in the next line are N space separated values of the array A. The last line of each test case contains two integers  x and y.

Output Format:
For each test case, print the required answer .

Your Task:
Your task is to complete the function minDist which returns  an integer denoting the minimum distance between two integers x and y in the array. If no such distance is possible then return -1.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= A, x, y <= 100

Example:
Input:
2
2
1 2
1 2
7
86 39 90 67 84 66 62 
42 12

Output:
1
-1

Explanation:
Testcase1: x=1 and y=2. minDistance between x and y is 1.
Testcase2: x=42 and y=12. We return -1 as the x and y don't exist in the array.
"""

import sys

def minDist(arr, n, x, y):
    mind = sys.maxsize
    
    for i in range(0,n):
        if (arr[i] == x or arr[i] == y):
            prev = i
            break
    
    for i in range(0,n):
        if (arr[i] == x or arr[i] == y):
            if (arr[prev] != arr[i] and (i - prev) < mind):
                mind = i - prev
                prev = i
            else:
                prev = i

    return mind if mind < sys.maxsize else -1

t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(minDist(arr, n, x, y))