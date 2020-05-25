import math
import numpy as np
import matplotlib.pyplot as plt
class curve:
    a, b, p, Gx, Gy=0, 0, 0, 0, 0
    def __init__(self):
        #Accepting the parameters necessary for the elliptic curve
        ctr = 0
        # Parameters a and b should satisfy (4*(a**3)) + (27*(b**2)) != 0
        while ctr == 0:
            self.a = int(input("Enter the curve parameter a: "))
            self.b = int(input("Enter the curve parameter b: "))
            val = (4*(self.a**3)) + (27*(self.b**2))
            if val != 0:
                ctr = 1
            else:
                print("Parameters a and b do not satisfy the conditions to be used in an elliptic curve")

        #Prime curve
        self.p = int(input("Enter a large prime number p: "))
        ctr = 0
        while ctr == 0:
            self.Gx = int(input("Enter the curve parameter Gx: "))
            self.Gy = int(input("Enter the curve parameter Gy: "))
            rhs = (self.Gx**3 + self.a*self.Gx + self.b) % self.p
            lhs = (self.Gy**2) % self.p
            if lhs == rhs:
                ctr = 1
            else:
                print("Point not on elliptic curve")

    def showParam(self):
        print(self.a)
        print(self.b)
        print(self.p)
        print(self.Gx)
        print(self.Gy)

    #Checks if point is on the curve
    def check(self, x, y):
        rhs = (x**3 + self.a*x + self.b) % self.p
        lhs = (y**2) % self.p
        if lhs == rhs:
            return True
        else:
            return False

obj = curve()
#Modular multiplicative inverse using fast power algorithm
def modulo_multiplicative_inverse(A, M):
    return fast_power(A, M-2, M)
    
def fast_power(base, power, MOD):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

#Addition of point to the generator point
def addition(O, Xq, Yq):
        sn = (O.Gy - Yq) % O.p
        sd = O.Gx - Xq
        sd = modulo_multiplicative_inverse(sd, O.p)
        s = (sn * sd) % O.p
        Xr = (s**2 - (O.Gx + Xq)) % O.p
        Yr = (s * (O.Gx - Xr) - O.Gy) % O.p
        return Xr, Yr

#Doubling the generator point
def double(O):
        sn = (3 * (O.Gx**2) + O.a) % O.p
        sd = 2 * O.Gy
        sd = modulo_multiplicative_inverse(sd, O.p)
        s = (sn * sd) % O.p
        Xr = (s**2 - 2*O.Gx) % O.p
        Yr = (s * (O.Gx - Xr) - O.Gy) % O.p
        return Xr , Yr

#Scalar multiplication on generator point
def scalar_multiplication(O, n):
    xr, yr = double(O)
    n = n - 2
    while (n != 0):
        xr, yr = addition(O, xr, yr)
        n = n - 1
        
    return xr, yr

x, y = scalar_multiplication(obj, 15)
print(x,y)
print(obj.check(x,y))
#print(modulo_multiplicative_inverse(5, 11))
'''
def bob():
    b = int(input("Enter Bob's private key: "))
    pbx, pby = obj.scalar_multiplication(b)
    return pbx, pby

def alice():
    a = int(input("Enter Alice's private key: "))
    pax, pay = obj.scalar_multiplication(a)
    return pax, pay

print(bob())
print(alice())
'''