def factors(n):
    factor=[]
    for i in range (1, n+1):
        if n % 1 == 0:
            factor.append(1)
    print(factor)
factors(int(input("what is the first number")))
