"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

def check(arr):
    arr = "".join(sorted(arr))
    for i in range(len(arr)-1):
        if (arr[i] == arr[i+1]):
            return False
    return True

arr = input()
print(check(arr))
