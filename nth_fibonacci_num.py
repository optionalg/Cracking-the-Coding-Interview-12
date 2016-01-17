# Write a method to generate the nth Fibonacci number.

# fib(n) -> fib(n - 1) + fib(n - 2)
# basecase -> fib(0) = 1; fib(1) = 1

fib_num = {0 : 1, 1 : 1}
def fib(n):
    if n in fib_num:
        return fib_num[n]
    else:
        fib_num[n] = fib(n - 1) + fib(n - 2)
        return fib_num[n]

print(fib(7))