"""
Given two square Matrices A[][] and B[][]. Your task is to complete the function multiply which stores the multiplied matrices in a new matrix C[][].
 
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the square matrix . Then in the next two lines are N*N space separated values of the matrix A[][] and B[][].
 
Output:
For each test case in a new line output will be the space separated values of the matrix C[][].
 
Constraints:
1<=T<=100
1 <= N <= 20
 
Example(To be used for the expected output):
Input:
2
2
7 18 2 9 
14 5 5 18 
2
17 4 17 16 
9 2 7 1 
Output:
188 359 73 172 
181 38 265 50 
"""
def multiply(A, B, C, n):
    for i in range (n):
        for j in range (n):
            for k in range (n):
                C[i][j] += A[i][k]*B[k][j]

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        matrix1 = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix1[i][j] = arr[c]
                c+=1
        arr = list(map(int, input().strip().split()))
        matrix2 = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix2[i][j] = arr[c]
                c+=1
        matrix3 = [[0 for i in range(n)]for j in range(n)]
        multiply(matrix1, matrix2, matrix3, n)
        for i in range(n):
            for j in range(n):
                print(matrix3[i][j], end=" ")
        print ('')

