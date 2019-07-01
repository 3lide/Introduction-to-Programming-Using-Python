def isValid(side1, side2, side3):
    if side1 + side2 > side3 and side1 > side1 - side2 and \
        side2 + side3 > side1 and side2 > side1 - side3 and \
        side1 + side3 > side2 and side3 > side2 - side1:
        return True
    else:
        return False

def main():
    side1, side2, side3 = eval(input(
        "Enter three edges: "
    ))
    if isValid(side1, side2, side3):
        print("The perimeter is {}".format(side1 + side2 + side3))
    else:
        print("The input is invalid") 

if __name__ == "__main__":
    main()