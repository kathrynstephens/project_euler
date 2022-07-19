# Solution to the Special Pythagorean triplet problem https://projecteuler.net/problem=9

# function to check if values a, b, and c
# form a pythagorean triplet
def is_pythagorean_triplet(a, b, c):
    if a < b < c:
        if ((a * a) + (b * b)) == (c * c):
            return True
        else:
            return False
    else:
        return False


# function to find Pythagorean triplets where
# a, b, c sum to N
def find_pythagorean_triplet_given_sum(n):
    # find digits that sum to n
    list_of_numbers = []
    for i in range(1, n + 1):
        for j in range(1, i):
            for k in range(1, j):
                temp = i + j + k
                if temp == n:
                    list_of_numbers.append([k, j, i])
    # check if numbers are a pythagorean triplet
    list_of_triplets = []
    for i in range(len(list_of_numbers)):
        temp = is_pythagorean_triplet(list_of_numbers[i][0], list_of_numbers[i][1], list_of_numbers[i][2])
        if temp:
            list_of_triplets.append(list_of_numbers[i])
    return list_of_triplets


if __name__ == '__main__':
    user_input = input("What number would you like the triplet to sum to?")
    possible_triplets = find_pythagorean_triplet_given_sum(int(user_input))
    print(possible_triplets)
    if len(possible_triplets) == 1:
        print(possible_triplets[0][0] * possible_triplets[0][1] * possible_triplets[0][2])
