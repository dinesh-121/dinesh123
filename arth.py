x=int(input("enter a value:"))
y=int(input("enter b value:"))
def arth(a,b):
    print("1.+\t2.-\t3.*\t4./\t5.%\t6.//\n")
    n=int(input("plz enter required operation:"))
    if n==1:
        print("a+b:",a+b)
    elif n==2:
        print("a-b:",a-b)
    elif n==3:
        print("a*b:",a*b)
    elif n==4:
        print("a/b:",a/b)
    elif n==5:
        print("a%b:",a%b)
    elif n==6:
        print("a//b:",a//b)
    else:
        print("plz enter valid operation")
arth(x,y)