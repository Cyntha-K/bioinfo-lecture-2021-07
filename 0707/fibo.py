def fibo(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo(n - 1) + fibo(n - 2)
    return result


n = input("number?")
n = int(n)
print(fibo(n))
