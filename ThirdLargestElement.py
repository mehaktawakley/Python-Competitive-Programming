def thirdLargest(arr, n):
    if(n<3):
        return -1
    else:
        arr.sort()
        return (arr[-3])

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int,input().strip().split()))
		print(thirdLargest(arr,n))
		

