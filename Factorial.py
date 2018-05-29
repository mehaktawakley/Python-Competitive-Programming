#WAP to print the factorial of a no using function.

def fact(num):
    factorial = 1

    if num==0:
        factorial = 1

    else:
        for i in range(1,num+1):
            factorial = factorial * i

    return factorial;


num = int(input("Factorial \nEnter a number:"))

print("Factorial of ", num, " is ", fact(num))
        
