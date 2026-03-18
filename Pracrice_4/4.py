def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a,b=map(int,input().split())
c=squares(a,b)
for j in c:
    print(j)