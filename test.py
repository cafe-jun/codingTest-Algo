def get_prime_nums():
    prime = [True] * 10000
    prime[0], prime[1] = False, False
    for i in range(2, 10000):
        if prime[i] == True:
            j = 2
            while i * j < 10000:
                prime[i * j] = False
                j += 1
    return prime


1.7881393432617188e-05
1.7881393432617188e-05
4.100799560546875e-05