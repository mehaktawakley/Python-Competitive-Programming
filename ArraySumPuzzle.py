"""
Given an array A of size N, construct a Sum Array S(of same size) such that S is equal to the sum of all the elements of A except A[i]. Your task is to complete the function SumArray(A, N) which accepts the array A and N(size of array).

Input :
The first line of input is the number of testcases T. Each of the test case contains two lines. The first line of which is an integer N(size of array). The second line contains N space separated integers.

Output :
For each test case print the sum array in new line.

User Task:
Since this is a functional problem you did not have to worry about the input. You just have to complete the function SumArray().

Constraint :
1 <= T <= 10
1 <= N <= 104
1 <= Ai <= 104

Example:
Input:
2
5
3 6 4 8 9
6
4 5 7 3 10 1

Output:
27 24 26 22 21
26 25 23 27 20 29

Explanation:
Testcase 1: For the sum array S, at i=0 we have 6+4+8+9. At i=1, 3+4+8+9. At i=2, we have 3+6+8+9. At i=3, we have 3+6+4+9. At i = 4, we have 3+6+4+8. So S is 27 24 26 22 21.
"""

{
#Initial Template for Python 3
def main():
    t = int(input())
    
    while(t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr,n)
        print ()
        t -= 1
        
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# arr is the array
# n is the number of element in array
def SumArray(arr,n):
    s = 0
    for i in range(n):
        s += int(arr[i])
    for i in range(n):
        print(s-int(arr[i]),end = ' ')