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


def compute_change_few_coins(amount):
    change = []
    money = [1, 0.25, 0.10, 0.05, 0.01]
    counter = 0
    for x in money:
        while amount >= x:
            counter += 1
            amount -= x
        change.append(counter)
        counter = 0
    return change


def binary_to_decimal(data):
    decimal = 0
    return decimal


def factorial(n):
    fac = "placeholder"
    return fac


def approx_pie(number):
    pi = "placeholder"
    return pi


def approx_e(number):
    e = "placeholder"
    return e

