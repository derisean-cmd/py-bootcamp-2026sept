# prime number identification
num = int(input("Enter the no. to check if it's prime no.: ")) # num that user wants to test if it's prime
is_prime = True

for x in range(2,num):   # the variable we want to check that within the range
    if num % x == 0:    # if the variable have zero remainder
        is_prime = False    # prime number is false

if is_prime == True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is NOT a prime number")