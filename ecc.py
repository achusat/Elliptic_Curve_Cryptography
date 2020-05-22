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

        self.p = int(input("Enter a large prime number p: "))
        self.N  = 8
        ctr = 0
        #Parameter M should satisfy M <= (p-8)/8
        """
        while ctr == 0:
            self.M = int(input("Enter value M for message mapping: "))
            if self.M <= (self.p-8)/8:
                ctr = 1
            else:
                print("M does not meet the condition to be used for message mapping")
        """
        while ctr == 0:
            self.Gx = int(input("Enter the curve parameter Gx: "))
            self.Gy = int(input("Enter the curve parameter Gy: "))
            rhs = (self.Gx**3 + self.a*self.Gx + self.b) % self.p
            lhs = self.Gy**2
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

    #checks if point is on the curve
    def check(self, x, y):
        rhs = (x**3 + self.a*x + self.b) % self.p
        lhs = y**2
        if lhs == rhs:
            return True
        else:
            return False
    



obj = curve()
obj.showParam()
print(obj.check(5,1))
