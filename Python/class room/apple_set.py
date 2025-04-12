def apples():
    n=int(input("Enter no of apples you want to buy :"))
    M1,P1=int((input("Enter no of apples per lot at shop-A:"))),int(input("Enter lot price of apples at shop-A:"))
    M2,P2=int((input("Enter no of apples per lot at shop-B:"))),int(input("Enter lot price of apples at shop-B:"))
    if n%M1==0:

        print("total cost of apples ={}".format(M1*P1))
    elif n%M2==0:
        print("total cost of apples={}".format(M2*P2))
    elif n%M1==0 and n%M2==0:
        print("total cost of apples={}".format(M1*P1))
    else:
        a,b=n%M1,n%M2
        print("no of apples more than lots with shop-A :{}".format(a),"no of apples more than lots with shop-B {}".format(b))
        a1,b1=n/M1,n/M2
        print(a1,b1)

x=apples()
# print(x)