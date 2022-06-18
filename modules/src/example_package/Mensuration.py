# AreaOfShapes module
# by Divyam Singhania

import variables

#Area of Triangle
def AreaTriangle(base, height):
    aTri = half * base * height
    return aTri

#Area of triangle by Heron's formula
def AreaTriangleH(LengthOfSide1, LengthOfSide2, LengthOfSide3):
    a = LengthOfSide1
    b = LengthOfSide2
    c = LengthOfSide3
    s = (a + b + c) / 2
    m = s * (s - a) * (s - b) * (s - c)
    ahTri = m ** 0.5
    return ahTri

#Area of Square
def AreaSquare(LengthOfSide):
    aSquare = LengthOfSide ** 2
    return aSquare

#Area of Rectangle
def AreaRectangle(length, breadth):
    aRec = length * breadth
    return aRec

#Area of Parallelogram
def AreaParallelogram(base, height):
    aPara = base * height
    return aPara

#Area of Trapezium
def AreaTrapezium(height, lengthofside1, lengthofside2):
    a = lengthofside1 + lengthofside2
    aTra = half * height * a
    return aTra

#Area of Circle
def AreaCircle(Radius):
    r = Radius
    aCir = π * sq(r)
    return aCir

#Area of Rhombus
def AreaRhombus(diagonal1, diagonal2):
    aRhom = half * diagonal1 * diagonal2
    return aRhom

#Area of regular Pentagon
#Penta => Pentagon
def AreaPenta(LengthOfSide):
    L = LengthOfSide
    L_square = L ** 2
    rb = 5 + 2 * root(5)
    root = 5 * rb * L_square
    aPen = 1/4 * root
    return aPen

#Area of regular Hexagon
#Hexa => Hexagon
def AreaHexa(LengthOfSide):
    L = LengthOfSide
    n = 3 * root(3)
    d = n / 2
    aHex = d * sq(L)
    return aHex

#Peri => Perimeter

#Perimeter of Square
def PeriSquare(LengthOfSide):
    L = LengthOfSide
    pSquare = L * 4
    return pSquare

#Perimeter of Rectangle
def PeriRectangle(length, breadth):
    L = length
    B = breadth
    LB = L + B
    pRec = 2 * LB
    return pRec

#Perimeter of Triangle
def PeriTriangle(LengthOfSide):
    L = LengthOfSide
    pTri = L * 3
    return pTri

#Perimeter of regular Pentagon
def PeriPenta(LengthOfSide):
    L = LengthOfSide
    pPen = L * 5
    return pPen

#Perimeter of regular Hexagon
def PeriHexa(LengthOfSide):
    L = LengthOfSide
    pHex = L * 6
    return pHex

#Perimeter of regular Heptagon
def PeriHepta(LengthOfSide):
    L = LengthOfSide
    pHep = L * 7
    return pHep

#Perimeter of regular Octagon
def PeriOcta(LengthOfSide):
    L = LengthOfSide
    pOct = L * 8
    return pOct

#Perimeter of regular Nonagon
def PeriNona(LengthOfSide):
    L = LengthOfSide
    pNon = L * 9
    return pNon

#Perimeter of regular Decagon
def PeriDeca(LengthOfSide):
    L = LengthOfSide
    pDec = L * 10
    return pDec

#Surface area => Sfa

#Surface area of cube
def SfaCube(LengthOfSide):
    L = LengthOfSide
    sCube = 6 * sq(L)
    return sCube

#Surface area of cuboid
def SfaCuboid(length, breadth, height):
    L = length
    B = breadth
    H = height
    b = L * B + B * H + H * L
    sCuboid = 2 * b
    return sCuboid

#Surface area of Cylinder
def SfaCylinder(radius, height):
    r = radius
    h = height
    cir = 2 * π * r
    sCy = cir * (r + h)
    return sCy

#Surface area of sphere
def SfaSphere(radius):
    r = radius
    sSphere = 4 * π * sq(r)
    return sSphere

#Surface area of hemisphere
def SfaHemisphere(radius):
    r = radius
    sHemi = 3 * π * sq(r)
    return sHemi

#Surface area of cone
def SfaCone(radius, height):
    r = radius
    h = height
    rh = sq(r) + sq(h)
    sCone = π * r * (r + sq(rh))
    return sCone

#Volume => Vol

#Volume of cube
def VolCube(LengthOfSide):
    l = LengthOfSide
    return cube(l)

#Volume of cuboid
def VolCuboid(length, breadth, height):
    l = length
    b = breadth
    h = height
    vCuboid = l * b * h
    return vCuboid

#Volume of Cylinder
def VolCylinder(radius, height):
    r = radius
    h = height
    vCy = π * sq(r) * h
    return vCy

#Volume of sphere
def VolSphere(radius):
    r = radius
    vSph = (4 / 3) * π * cube(r)
    return vSph

#Volume of hemisphere
def VolHemi(radius):
    r = radius
    vHemi = (2 / 3) * π * (cube(r))
    return vHemi

#Volume of cone
def VolCone(radius, height):
    r = radius
    h = height
    vCone = π * sq(r) * h / 3
    return vCone

#Pythagoras Theorem
def pytha(LengthOfPerpendicular, LengthOfBase):
    p = LengthOfPerpendicular
    b = LengthOfBase
    hsq = sq(p) + sq(b)
    H = root(hsq)
    return H

# Circumference
def circum(radius):
    r = radius
    Circumference = 2 * π * r
    return Circumference