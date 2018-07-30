"""
Raghav is given a task to select at most 10 employees for a company project. Each employee is  represented by a single digit I.D. number which is unique for all the selected employees of the project. Raghav has a technical problem in his system which printed I.D. number multiple times. Help him to get rid of the repeated numbers.
Input:
First line contain T test cases. Second line contain the Total number (N) of employees where repeated I.Ds. are present. Third line contain the array A[N] of size N containing the I.Ds. of employees.
Output:
Print the non repeated selected I.D. of employees in a new line in the same sequence they appear in Input.
Constraints:
1<=T<=100
0<=N<=1000
Example:
Input:
5
5
8 8 6 2 1
6
7 6 7 4 2 7
9
1 9 6 7 4 8 1 4 5
3
1 1 1
5
0 1 0 1 2
Output:
8 6 2 1
7 6 4 2
1 9 6 7 4 8 5
1
0 1 2
"""
count = int(input())

while count>0:
    input()
    n = list(map(int,input().split()))
    n1 = []
    for i in n:
        if i not in n1:
            n1.append(i)
    print(*n1)
    count-=1
