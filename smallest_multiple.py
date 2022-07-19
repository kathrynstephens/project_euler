# Solution to Smallest Multiple problem https://projecteuler.net/problem=5

# Find the smallest number that can be evenly divided by all
# numbers between 1 and N
def smallest_multiple(range_end):
    factors = range(1, range_end)
    num = range_end
    flag = True
    while flag:
        divisible = 0
        for m in factors:
            if (num % m) != 0:
                break
            else:
                divisible = divisible + 1
        if divisible == (range_end - 1):
            flag = False
            return num
        else:
            num = num + range_end


if __name__ == '__main__':
    divisible_range: str = (input("I would like the number to be evenly divisible by all numbers in the range 1 to "))
    multiple = smallest_multiple(int(divisible_range))
    print(multiple)
