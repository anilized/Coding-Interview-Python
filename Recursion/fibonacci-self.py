# 0,1,1,2,3,5,8,13,21
# Solve fibonacci with recursive
# Given a number N return the index value of the Fibonacci seq

def fibonacciRec(n):
    if n <= 1:
        return n
    return (fibonacciRec(n-1) + fibonacciRec(n-2))

nterms = int(input("How many terms"))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibo")
    for i in range(nterms):
        print(fibonacciRec(i))