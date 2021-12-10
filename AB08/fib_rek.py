print("Unendlicher Fibonacci Generator")

zahl1 = 0
zahl2 = 1

def fibonacci(a, b):
    while True:
        yield a
        a, b = b, a + b

f = fibonacci(zahl1, zahl2)

counter = 0

for x in f:
    print("fib(" + str(counter) + ") = " + str(x))
    counter += 1
    if (counter > 25): break
