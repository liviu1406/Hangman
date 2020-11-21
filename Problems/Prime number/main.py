n = int(input())

# prime numbers are greater than 1
if n > 1:
    # check for factors
    for i in range(2, n):
        if (n % i) == 0:
            print("This number is not prime")
            # print(i, "times", n // i, "is", n)
            break
    else:
        print("This number is prime")
# if input number is less than
# or equal to 1, it is not prime
else:
    print("This number is not prime")
