# Solution to Largest Product in a Series problem https://projecteuler.net/problem=8

# For a series represented as a number, find the largest product of
# N digits
def largest_product_in_series(digits, number):
    # find the number of digits in the series
    len_of_number = len(number)
    print(len_of_number)
    # if the number of digits in the series is less than
    # or equal to the number of digits being multiplied,
    # return the product of all digits of the number
    if len_of_number <= digits:
        temp = 1
        for n in range(len_of_number):
            temp = temp * number[n]
        return temp

    # if the number of digits in the series is greater than
    # the number of digits being multiplied, find the greatest
    # product of n digits
    largest_product = 1
    for n in range(digits-1, len_of_number):
        temp = 1
        for i in range(digits):
            temp = temp * int(number[n - i])
        if temp > largest_product:
            print(str(n) + ": " + str(largest_product))
            largest_product = temp
    return largest_product


if __name__ == '__main__':
    user_input = input("How many digits would you like to multiply?")
    Number_of_digits = int(user_input)
    print(Number_of_digits)
    Number = "73167176531330624919225119674426574742355349194934969835203127" \
             "74506326239578318016984801869478851843858615607891129494954595" \
             "01737958331952853208805511125406987471585238630507156932909632" \
             "95227443043557668966489504452445231617318564030987111217223831" \
             "13622298934233803081353362766142828064444866452387493035890729" \
             "62904915604407723907138105158593079608667017242712188399879790" \
             "87922749219016997208880937766572733300105336788122023542180975" \
             "12545405947522435258490771167055601360483958644670632441572215" \
             "53975369781797784617406495514929086256932197846862248283972241" \
             "37565705605749026140797296865241453510047482166370484403199890" \
             "00889524345065854122758866688116427171479924442928230863465674" \
             "81391912316282458617866458359124566529476545682848912883142607" \
             "69004224219022671055626321111109370544217506941658960408071984" \
             "03850962455444362981230987879927244284909188845801561660979191" \
             "33875499200524063689912560717606058861164671094050775410022569" \
             "83155200055935729725716362695618826704282524836008232575304207" \
             "52963450"
    print(largest_product_in_series(Number_of_digits, Number))
