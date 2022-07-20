# Solution to the Summation of Primes problem https://projecteuler.net/problem=10

from largest_prime_factor import gen_primes


# Function to sum the primes below n
def sum_primes(n):
    s = 0
    prime_generator = gen_primes()
    p = next(prime_generator)
    while p < n:
        s = s + p
        p = next(prime_generator)
    return s


if __name__ == '__main__':
    user_input = input("I would like to sum all the primes below ")
    prime_limit = int(user_input)
    sum_of_primes = sum_primes(prime_limit)
    print(sum_of_primes)
