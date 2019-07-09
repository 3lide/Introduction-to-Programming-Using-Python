from LinearEquation import LinearEquation

def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
    linearequation = LinearEquation(a, b, c, d, e, f)
    if linearequation.isSolvable():
        print("The linearequation's solutions are", linearequation.getX(), 
        "and", linearequation.getY())
    else:
        print("The linearrquation has no solution.")

if __name__ == "__main__":
    main()