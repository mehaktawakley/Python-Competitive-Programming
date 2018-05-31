"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""

num = [] #Empty List
pos = 0

num = list(map(int,input().split()))
target = int(input())
pos = 0

lb = 0
ub = len(num)-1
mid = (lb+ub)//2

while(lb<=ub): #Binary Search
    if (num[mid] == target):
        pos = mid
        break;
        
    elif (target < num[mid]):
        ub = mid-1
        
    elif (target>num[mid]):
        lb = mid+1
        
    mid = (lb+ub)//2

    if(lb>ub): #If element not found
        pos = lb

print (pos)
