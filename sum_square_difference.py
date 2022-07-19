# Solution to the Sum Square Difference problem https://projecteuler.net/problem=6

# Function to calculate the sum of
# the square of the fist N natural numbers
def sum_of_squares(n):
    s = 0
    for m in range(1, n+1):
        s = s + (m * m)
    return s


# Function to calculate the square
# of the sum of the first N natural numbers
def square_of_sum(n):
    s = (n * (n + 1)) / 2
    sq = s * s
    return sq


# Function to find the difference between
# the sum of squares and the square of sum
# of first N natural numbers
def difference_sum_square(n):
    m = sum_of_squares(n)
    p = square_of_sum(n)
    if m > p:
        difference = m - p
    else:
        difference = p - m
    return difference


if __name__ == '__main__':
    range_of_natural_nums: str = (input(
        "I would like the difference between the sum of squares and the square of sum for natural numbers up to  "))
    print(difference_sum_square(int(range_of_natural_nums)))
