import numpy as np
def is_prime(n):
    for i in range(2, int(np.sqrt(n))):
        if n%i == 0:
            return i
    return 0

is_prime(4141)