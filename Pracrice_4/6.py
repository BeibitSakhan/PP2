def fibo(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
a=int(input())
c=fibo(a)
f=True
for j in c:
    if not f:
        print(',',end="")
    print(j,end="")
    f=False