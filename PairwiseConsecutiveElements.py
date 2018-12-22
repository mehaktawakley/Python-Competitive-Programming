"""
Given a stack of integers of size N, your task is to complete the function pairWiseConsecutive(), that checks whether numbers in the stack are pairwise consecutive or not. The pairs can be increasing or decreasing, and if the stack has an odd number of elements, the element at the top is left out of a pair. The function should retain the original stack content.
Only following standard operations are allowed on stack.
push(X): Enter a element X on top of stack.
pop(): Removes top element of the stack.
empty(): To check if stack is empty.


Examples:
Input : stack = [4, 5, -2, -3, 11, 10, 5, 6, 20]
Output : Yes
Each of the pairs (4, 5), (-2, -3), (11, 10) and
(5, 6) consists of consecutive numbers.

Input : stack = [4, 6, 6, 7, 4, 3]
Output : No
(4, 6) are not consecutive.

Input:
The function takes a single argument as input, a stack object 's' of type int that contain the elements.
There will be T test cases and for each test case the function will be called separately.

Output:
For eachtestcase output a single line containing "Yes"(without quote) if the elements of the stack is pairwise consecutive, else print "No".

Constraints:
1<=T<=100
1<=N<=103

Example:
Input:
2
6
1 2 3 4 5 6
5
1 5 3 9 7
Output:
Yes
No
"""

{
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        pairWiseConsecutive(l)
        if(pairWiseConsecutive(l)==True):
            print("Yes")
        else:
            print("No")
}

def pairWiseConsecutive(l):
    temp = l.copy()
    n = len(temp)
    
    if (len(l) % 2 != 0):
        temp.pop()
    
    while temp:
        a,b = temp.pop(), temp.pop()
        if abs(a-b) != 1:
                return False
    return True
        