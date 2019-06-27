weightInPounds = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inch = eval(input("Enter inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
INCHES_PER_FEET = 12

weightInKilograms = weightInPounds * KILOGRAMS_PER_POUND
heightInMeters = (feet * INCHES_PER_FEET + inch) * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is",format(bmi, ".2f"))
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
