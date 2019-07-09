from RegularPolygon import RegularPolygon

regularpolygon1 = RegularPolygon()
regularpolygon2 = RegularPolygon(6, 4)
regularpolygon3 = RegularPolygon(10, 4, 5.6, 7.8)

print("regularpolygon1's perimeter is", regularpolygon1.getPerimeter(), 
"and its area is", regularpolygon1.getArea())
print("regularpolygon2's perimeter is", regularpolygon2.getPerimeter(), 
"and its area is", regularpolygon2.getArea())
print("regularpolygon3's perimeter is", regularpolygon3.getPerimeter(), 
"and its area is", regularpolygon3.getArea())