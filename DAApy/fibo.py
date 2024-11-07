def recursive_fibo(n):
    if n<=1:
        return n
    else:
        return recursive_fibo(n-1)+recursive_fibo(n-2)


def non_recursive_fibo(n):
    first=0
    second=1
    print(first,end=" ")
    print(second,end=" ")
    while n-2>0:
        third=first+second
        first=second
        second=third
        print(third,end=" ")
        n-=1;
    print()

if __name__=="__main__":
    n=int(input("enter the numbers: "))
    print ("recursive serie :")
    for i in range (n):
        print(recursive_fibo(i),end=" ")
    print()

    print("Non-recursive series:")
    non_recursive_fibo(n)
