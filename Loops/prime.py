lower = int(input("Enter start "))
upper = int(input("Enter end "))

print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True
        for i in range(2, (num//2)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
