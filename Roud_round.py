def round_and_round(n, b, a):
    if n == 0:
        return 0
    
    final_position = (a + b) % n
    
    if final_position == 0:
        return n
    else:
        return final_position
