"""
Given a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. You are given a number N, you have to print the number of integers less than N in the sample space S.

Input :
The first line contains an integer T, denoting the number of test cases.Then T test cases follow. The first line of each test case contains an integer N, denoting the number.

Output :
Print the answer of each test case in a new line.

Constraints :
1<=T<=100
1<=N<=10^18

Example
Input :
2
9
3

Output :
2
1
"""

def checksqrt(n):
    if n == 0:
        return 0
    
    else:
        start, end = 1, n
        while (start <= end):
            mid = (start+end) // 2
            sqrt = mid * mid
            if sqrt == n:
                return (mid-1)
            else:
                if sqrt > n:
                    end = mid - 1
                else:
                    start = mid + 1
        return end
        

t = int(input())

while(t>0):
    n = int(input())
    print(checksqrt(n))
    t -= 1
