# Solution to Largest Palindrome Product problem

# function to check if number is
# palindrome or not
def is_palindrome(n):
    # Skip single-digit inputs
    if n // 10 == 0:
        return False
    # convert integer to string
    s = str(n)
    # Using predefined function to
    # reverse to string print(s)
    rev: str = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if s == rev:
        return True
    return False


# function to find the largest palindrome
# that is the product of 2 n-digit numbers
def largest_palindrome_product(digits):
    smallest_multiple = pow(10, digits - 1)
    largest_multiple = pow(10, digits) - 1
    print(smallest_multiple, largest_multiple)
    list_of_numbers = range(largest_multiple, smallest_multiple, -1)
    list_of_multipliers = list(range(largest_multiple, smallest_multiple, -1))
    palindrome = 0
    for n in list_of_numbers:
        for m in list_of_multipliers:
            if is_palindrome(n * m):
                if (n*m) > palindrome:
                    palindrome = n*m
        list_of_multipliers.remove(n)
    return palindrome


if __name__ == '__main__':
    number_of_digits = (input("How many digits should the multiples have?"))
    largest_palindrome = largest_palindrome_product(int(number_of_digits))
    print(largest_palindrome)
