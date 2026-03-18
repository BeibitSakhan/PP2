def rev(a):
    for i in range(0,a+1):
        yield i
s=int(input())
c=rev(s)
b=list(c)[::-1]
for j in b:
    print(j)