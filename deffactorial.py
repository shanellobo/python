def fact(num):
    fact=1
    for i in range(1,num + 1):
        fact=fact*i
    print("The factorial of",num,"is",fact)
num=int(input("enter a number"))
fact(num)
