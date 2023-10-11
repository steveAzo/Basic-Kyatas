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