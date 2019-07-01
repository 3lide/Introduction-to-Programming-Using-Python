number = eval(input("Enter an integer: "))

print("Is {} divisible by 5 and 6?".format(number), \
    number % 5 == 0 and number % 6 == 0)
print("Is {} divisible by 5 or 6?".format(number), \
    number % 5 == 0 or number % 6 == 0)
print("Is {} divisible by 5 or 6, but not both?".format(number), \
    (number % 5 == 0 and number % 6 != 0) or (
        number % 6 == 0 and number % 5 != 0
    ))