import numpy as np
import pandas as pd
import math

c_1 = input()
c_2 = input()

C_1 = c_1.split(' ')
C_2 = c_2.split(' ')

A = []
B = []
C = []

for i in C_1:
     A.append(float(i))

for i in C_2:
     B.append(float(i))



#for i in range(5):
#     d = math.log2(B[i]+1) - math.log2(A[i]+1)
#     C.append([A[i],B[i],d])

for i in range(5):
     d = math.log2(C_1[i]+1) - math.log2(C_2[i]+1)
     C.append([C_1[i],C_2[i],d])

F = pd.DataFrame(C,index =  ['ACTB','MAPT','GAPDH','TP53','PSAP'] , columns = ['ctrl' , 'treated' , '12fc'])

print(F)