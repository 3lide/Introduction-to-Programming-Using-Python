from QuadraticEquation import QuadraticEquation

def main():
    a = eval(input("Enter a: "))
    b = eval(input("Enter b: "))
    c = eval(input("Enter c: "))
    quadraticequation = QuadraticEquation(a, b, c)
    if quadraticequation.getDescriminant() > 0:
        print("The quadraticequation's roots is", quadraticequation.getRoot1(), 
        "and", quadraticequation.getRoot2())
    elif quadraticequation.getDescriminant() == 0:
        print("The quadraticequation has only one root, and the root is", 
        quadraticequation.getRoot1())
    else:
        print("The quadraticequation has no real root")

if __name__ == "__main__":
    main()