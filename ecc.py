import math
import numpy as np
import matplotlib.pyplot as plt
class Cryptography:
    a,b,p,N,M=0,0,0,0,0
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
                print("Parameters a and b do not satisfy the conditions to be used in an ellitic curve")

        self.p = int(input("Enter a large prime number p: "))
        self.N  = 8
        ctr = 0
        #Parameter M should satisfy M <= (p-8)/8
        while ctr == 0:
            self.M = int(input("Enter value M for message mapping: "))
            if self.M <= (self.p-8)/8:
                ctr = 1
            else:
                print("M does not meet the condition to be used for message mapping")
    def showParam(self):
        print(self.a)
        print(self.b)
        print(self.p)
        print(self.M)
        print(self.N)

obj = Cryptography()
obj.showParam()
