"""
def prime(sum1):
    for i in range(2,(sum1//2)+1):
        if (sum1%i==0):
            return False
    return True

count = int(input())

while count>0:
    input()
    sum1 = 0
    string = input()
    for i in string:
        sum1+=ord(i)
    
    print("YES" if prime(sum1) else "NO")
    count-=1
"""

sdef prime(sum1):
    for i in range(2,(sum1//2)+1):
        if (sum1%i==0):
            return False
    return True

count = int(input())

while count>0:
    input()
    sum1 = 0
    string = input()
    for i in string:
        sum1+=ord(i)
    
    print("YES" if prime(sum1) else "NO")
    count-=1
