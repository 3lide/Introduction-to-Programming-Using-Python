weightInPounds = eval(input("Enter weight in pounds: "))
heightInInches = eval(input("Enter height in inches: "))

weightInKg = weightInPounds * 0.45359237
heightInMeters = heightInInches * 0.0254
BMI = weightInKg / heightInMeters ** 2

print("BMI is", format(BMI, ".4f"))