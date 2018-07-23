count = int(input())

while count>0:
    a = list(map(int,input().split()))
    print(((a[0]//2)+1)*a[1] if (a[0]%2 == 1) else ((a[0]//2)*a[1]))
    count-=1
