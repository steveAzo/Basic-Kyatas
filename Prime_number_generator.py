def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True
        
def find_prime(n):
    lists = []
    for i in range(0, n + 1):
        if is_prime(i):
            lists.append(i)
    return lists
    
