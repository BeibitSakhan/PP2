def thrfor(a):
    for i in range(0,a+1):
        if i%3==0 and i%4==0:
            yield i
a=int(input())
c=thrfor(a)
san=True
for j in c:
    if not san:
        print(' ',end='')
    print(j,end='')
    san=False