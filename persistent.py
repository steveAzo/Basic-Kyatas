def persistence(n):
    # your code
    product = 1
    num_str = str(n)
    if n < 10:
        return 0
    for i in num_str:
        digit = int(i)
        product *= digit
        
    return 1 + persistence(product)

n = input("What number do you want to check out? ")
try:
    number = int(n)
    result = persistence(number)
    print(f"The multiplicative persistence of {number} is {result}")

except ValueError:
    print("Invalid input, Please enter a valid number:")
