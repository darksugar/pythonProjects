#Authon Ivor

def fib(max):
    n,a,b=0,0,1
    for n in range(max):
        yield b
        a,b=b,a+b
    return "done"

f = fib(15)
for i in f:
    print(i)