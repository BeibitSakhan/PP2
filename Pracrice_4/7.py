class anon:
    def __init__(self,san):
        self.san=san
        self.pos=len(san)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos<0:
            raise StopIteration
        char=self.san[self.pos]
        self.pos-=1
        return char
a=input()
for sa in anon(a):
    print(sa,end="")