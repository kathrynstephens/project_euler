# Solution to 10001st prime problem https://projecteuler.net/problem=7
from largest_prime_factor import gen_primes


def nth_prime_number(n):
    list_of_primes = gen_primes()
    for m in range(1, n):
        next(list_of_primes)
    return next(list_of_primes)


if __name__ == '__main__':
    user_input = input("What prime would you like?")
    Number = int(user_input)
    prime_number = nth_prime_number(Number)
    print(prime_number)
