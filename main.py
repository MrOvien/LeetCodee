# fibonaci
n=20500
a=1
b=1
# print(a)
# print(b)
def Fibonacci(n,a,b):
    for i in range(2,n):
       c=a+b
       # print(c)
       a=b
       b=c
    print("Fibonacci Number:", end=" ")
    return c

print(Fibonacci(n,a,b))
