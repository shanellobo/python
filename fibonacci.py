num=int(input("enter a number"))
n1,n2=0,1
print("the fibonacci sequence is")
print(n1)
print(n2)
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
