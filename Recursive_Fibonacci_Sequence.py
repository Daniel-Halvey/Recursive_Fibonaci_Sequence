def recur_fib(n):
    if n <= 1:
        return n
    else:
        return (recur_fib(n - 1) + recur_fib(n - 2))
n_terms = 20
if n_terms <= 0:
    print("Please input positive integer")
else:
    print("*")
    print("**")
    print("***")
    print("*****")
    print("********")
    print("Fibonacci Sequence:")
    for i in range(n_terms):
        print(recur_fib(i))
        print("Patterns are everywhere")
        print("12345678")
        print("12345")
        print("123")
        print("12")
        print("1")