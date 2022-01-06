import numpy as np
import scipy.linalg

#Linear Regression using Singular Value Decomposition (Machine Learning)

#(WILL NOT WORK UNTIL YOU LINK YOUR OWN JSON DATA SET FILE OR CREATE YOUR OWN ARRAY(S))

'''
import json
from re import I
from scipy.linalg import svdvals
f = open("C:/.../.../.../LINK_FILE_LOCATION_HERE.json") 
data = json.load(f) 
A = np.array(data) 
u, s, vt = scipy.linalg.svd(A) 
print("U =") 
print(u)
print()
print("S =")
print(s)
print()
print("V^T =")
print(vt)
print()

#Hardcoded Version of SVD to compare prediction vs actual value.
C = A.T @ A
E, F = scipy.linalg.eig(C) 
B = np.sqrt(E)
C or D.
D = A @ A.T 
G, H = scipy.linalg.eig(D)
print() 
print("Hardcoded U =")
print(H)
print()
print("Hardcoded S =")
print(B)
print()
print("Hardcoded V^T =")
print(F)
'''

#Linear Algebra Continued

#Question1
A = np.array([[10, -7, 0], [-3, 2, 6], [5, -1, 5]]) #Here I am creating the array in Python.
P, L, U = scipy.linalg.lu(A) #Here I am performing LU Decomposition using scipy.linalg.lu()
print("Question 1:")
print("P = ") #Everything after this is me printing the information to the screen.
print(P)
print()
print("L = ")
print(L)
print()
print("U = ")
print(U)
print()

#Question2
B = np.array([[10, -7, 0], [-3, 2, 6], [5, -1, 5]]) #Here I am creating the array in Python.
u, s, vt = scipy.linalg.svd(B) #Here I am using the scipy.linalg.svd() function to calculate the SVD of the array.
print("Question 2:")
print("U = ")
print(u)
print()
print("S = ")
print(s)
print()
print("V^T = ")
print(vt)
print()

#Question3
C = np.array([[10, -7, 0], [-3, 2, 6], [5, -1, 5]]) #Here I am creating the array in Python.
Q, R = scipy.linalg.qr(C) #Here I am using the scipy.linalg.qr() to compute QR decomposition.
print("Question 3:")
print("Q = ") #Everything after this is me printing the values to the screen.
print(Q)
print()
print("R = ")
print(R)
print()