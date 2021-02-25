import random


def create_bill_number(is_visa):
    odd_digits = ['1', '3', '5', '7', '9']
    even_digits = ['2', '4', '6', '8', '0']
    digits = odd_digits + even_digits
    first_digit = random.choice(even_digits) if is_visa else random.choice(odd_digits)
    return first_digit + ''.join(random.sample(digits, 9))
