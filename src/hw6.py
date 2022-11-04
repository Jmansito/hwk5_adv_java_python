# Split number function to return the join of the string with a space


def split_number(number):
    return ' '.join(str(number))

# Palindrome function: Will assign the received number to a holder
# Then create a reversed number in the while loop
# compare the two numbers then return the boolean result


def is_palindrome(number):
    reversed_num = 0
    holder = number
    while number > 0:
        remainder = number % 10
        reversed_num = (reversed_num * 10) + remainder
        number = number // 10
    if reversed_num == holder:
        return True
    else:
        return False

# Compute variance of an arbitrary number of arguments
# Find the mean -> compute standard dev -> return standard dev / number of args


def compute_variance(*args):
    standard_dev = 0
    mean = sum(args) / (len(args))
    for arg in args:
        standard_dev += pow((arg - mean), 2)
    return (1 / ((len(args)) - 1)) * standard_dev

# compute variance req requires two arguments
# Does the same as compute_variance


def compute_variance_req(arg1, arg2, *args):
    args = list(args)
    args.append(arg1)
    args.append(arg2)
    standard_dev = 0
    mean = sum(args) / (len(args))
    for arg in args:
        standard_dev += pow((arg - mean), 2)
    return (1 / ((len(args)) - 1)) * standard_dev


# Compute change function
# First build the list for money that will be used to check
# loop through the money list, then in inner list add to the coin counter until we reach the point
# where adding another of that value would send it over the change amount
# return tuple of the coins needed for change


def compute_change_few_coins(amount):
    change = []
    money = [1, 0.25, 0.10, 0.05, 0.01]
    counter = 0
    for x in money:
        while round(amount, 2) >= x:
            counter += 1
            amount -= x
        change.append(counter)
        counter = 0
    return tuple(change)


# Binary -> decimal conversion.
# loop through the data from right to left  (from book)
# Check if the number in the position is a 1 then add the value of i to decimal
# i increments * 2 each loop

def binary_to_decimal(data):
    decimal, i = 0, 1
    numbers = []
    numbers += data

    for num in range((len(numbers)-1), -1, -1):
        if numbers[num] == '1':
            decimal += i
        i *= 2
    return decimal


# Factorial function that will return the factorial of a given number after making sure the number is not negative or 0


def factorial(n):
    fac = 1
    # First check if the number is negative or 0
    if n < 0:
        return "Does not exist"
    elif n == 0:
        return 1
    else:
        # Loop through the range and run factorial algorithm
        for num in range(1, n + 1):
            fac *= num
    return fac


# Equation given is Leibniz's formula (I am using my python code from my algorithms course for this)
# Number is how many times we will iterate
# Check if we are on an even or odd number
# add if we are on even, subtract if we are on negative using Leibniz's formula

def approx_pie(number):
    denominator, pi = 1, 0
    # The 4 in the equation is being ignored in the auto grader, so + 1 to the loop
    for num in range(number + 1):
        if num % 2 == 0:
            pi += 4 / denominator
        else:
            pi -= 4 / denominator
        denominator += 2

    return pi


# Approximate e using factorial function for the denominator in our loop

def approx_e(number):
    e = 0
    for num in range(number):
        e += (1 / factorial(num))
    return e
