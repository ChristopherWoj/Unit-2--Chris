num1 = 10
num2 = 25

# Greatest Common Factor using the Euclidean algorithm
while num2 != 0:
    num1, num2 = num2, num1 % num2

print("The GCF is:", num1)

