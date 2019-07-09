from Fan import Fan

fan1 = Fan(3, 10, "yellow", True)
fan2 = Fan(2, 5, "blue", False)

print("fan1's speed is", fan1.getSpeed(), "radius is", fan1.getRadius(), 
"color is", fan1.getColor(), "on is", fan1.getOn())

print("fan2's speed is", fan2.getSpeed(), "radius is", fan2.getRadius(), 
"color is", fan2.getColor(), "on is", fan2.getOn())