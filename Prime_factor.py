def is_prime(number):
    if number <=1:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True

def prime_factors(fac):
    lists = []
    for i in range(0, fac + 1):
        while is_prime(i) and fac % i == 0:
            lists.append(i)
            fac //= i 
    return lists    

fac = int(input("Please what number do you wanna list the prime factors?:"))
print(f"The prime factors of {fac} is: ", prime_factors(fac))
print("Feel free to ask me any question, Cuz I have turn into a robot")
            
