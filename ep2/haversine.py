from math import radians, cos, sin, asin, sqrt

def haversine(r,f1,l1,f2,l2):
    a = (sin(radians(f2-f1)/2))**2
    b = (sin(radians(l2-l1)/2))**2
    d = cos(radians(f1))*cos(radians(f2))
    e = 2*r*asin(sqrt(a + b*d))
    return e
