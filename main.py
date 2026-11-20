import prg30.rectangle

import prg30.circle

import prg30.Dgraphics.cubid

import prg30.Dgraphics.sphere

print("Rectangle")

l=int(input("enter the length: "))

b=int(input("enter the breadth: "))

print("Area:", prg30.rectangle.area(l, b))

print("perimeter:",prg30.rectangle.perimeter(l, b))



print("Circle")

r = int(input("Enter the radius: "))

print("Area:", prg30.circle.area(r))

print("Perimeter:", prg30.circle.perimeter(r))


print("cuboid")

lc=int(input("enter the length cube:  "))

bc=int(input("enter the breadth cube:  "))

hc=int(input("enter the height cube:"  ))

print("Area:",prg30.Dgraphics.cubid.area(lc, bc, hc))

print("perimeter:",prg30.Dgraphics.cubid.perimeter(lc, bc,hc))



print("Sphere")

rs = int(input("Enter the radius of sphere: "))

print("Area:",prg30.Dgraphics.sphere.area(rs))

print("Volume:", prg30.Dgraphics.sphere.volume(rs))