from Rectangle import Rectangle

def main():
    rectangle1 = Rectangle(4, 40)
    rectangle2 = Rectangle(3.5, 35.7)
    print("rectangle1's width is", rectangle1.width,"height is", 
    rectangle1.height, "area is", rectangle1.getArea(), 
    "perimeter is", rectangle1.getPerimeter())

    print("rectangle2's width is", rectangle2.width, "height is", 
    rectangle2.height, "area is", rectangle2.getArea(), 
    "perimeter is", rectangle2.getPerimeter())

if __name__ == "__main__":
    main()