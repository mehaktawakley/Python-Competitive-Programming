"""
Ishaan has bought N lottery tickets each having an ID denoted by an array A. As the result comes out, Ishaan gets very lucky and gets to know that each one of his tickets has won some prize. But unfortunately, he can't claim all of his lottery tickets.
The "sum_id" of a lottery ticket is the sum of the individual digits of the ticket ID. For example, sum_id of a ticket with ID = 1234 is 1+2+3+4 = 10.
Ishaan can claim the prize of a ticket only if no other ticket with the same sum_id has been claimed by him yet (Refer example for explanation).
Find out the maximum number of tickets he can claim.

Input : 
First line of input contains a single integer T denoting the number of test cases.
The first line of each test case contains an integer N.
The second line contains N space-separated integers denoting the array A.

Output : 
For each test case, print the required answer in a new line.

Constraints : 
1 <= T <= 100
1 <= N <= 5000
1 <= A[i] <= 10^15

Example : 
Input : 
3
5
123 42 45 78 12345
6
2 3 4 6 22 8
4
45 333 1323 9
Output : 
3
5
1

Explanation : 
Case 1 : 
sum_id of Ticket 1 : 1+2+3 = 6 (claimed)
sum_id of Ticket 2 : 4+2 = 6 (can't be claimed since Ticket 1 with same sum_id has already been claimed)
sum_id of Ticket 3 : 4+5 = 9 (claimed)
sum_id of Ticket 4 : 7+8 = 15 (claimed)
sum_id of Ticket 5 : 1+2+3+4+5 = 15 (can't be claimed since Ticket 4 with same sum_id has already been claimed)

Case 2 : 
sum_id of Ticket 1 : 2 (claimed)
sum_id of Ticket 2 : 3 (claimed)
sum_id of Ticket 3 : 4 (claimed)
sum_id of Ticket 4 : 6 (claimed)
sum_id of Ticket 5 : 2+2 = 4 (can't be claimed since Ticket 3 with same sum_id has already been claimed)
sum_id of Ticket 4 : 8 (claimed)
"""

count = int(input())

while count>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in a:
        summ = 0
        while i > 0:
            summ += (i%10)
            i //= 10
        if summ not in b:
            b.append(summ)
    print(len(b))
    
    count-=1
