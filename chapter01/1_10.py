distance = eval(input("Enter the distace in km(eg:45): "))
time = eval(input("Enter the time in min(eg:2.4): "))

print("The velocity is {:.2f} mile/h.".format(distance / 1.6 / (time / 60)))
