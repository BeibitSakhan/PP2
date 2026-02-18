def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2) # Теперь double — это лямбда x: x * 2
triple = make_multiplier(3) # Теперь triple — это лямбда x: x * 3

print(double(10)) # 20
print(triple(10)) # 30