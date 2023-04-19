#-----------------------con el dato estructurado list-------------------------
#Lista de listas (Matriz)
m = [[1,2,3,6,8],[5,6,7,6,0],[8,9,0,3,2],[3,4,5,4,6]]

#Matriz 
for lista in m:
    print(lista)
print()

#Elemento de la matriz
print("Elemento de una matriz: ",m[3][2],sep= "\n",end= "\n\n")
#Renglon de una matriz
print("Renglon de una matriz: ",m[2][:],sep= "\n",end= "\n\n")
#Columna de una matriz
print("Columna de una matriz: ")
for lista in m:
    print(lista[3],end=" ")
print("\n\n")

#---------------------con numpy---------------------------------
import numpy as np

M = np.array([[1,2,3,6,8],[5,6,7,6,0],[8,9,0,3,2],[3,4,5,4,6]])

#Matriz
print(M,end= "\n\n")
#Elemento de una matriz
print("Elemento de una matriz: ",M[3][2],sep= "\n",end= "\n\n")
print("Elemento de una matriz como una submatriz: ",M[3:4,2:3],sep= "\n",end= "\n\n")
#Renglon de una matriz
print("Renglon de una matriz: ",M[2][:],sep= "\n",end= "\n\n")
#Columna de una matriz
print("Columna de una matriz: ",M[:,3],sep= "\n",end= "\n\n")
#Submatriz
print("Submatriz: ",M[1:3,2:4],sep= "\n",end= "\n\n")

#Operaciones con numpy
print(M.diagonal()) #Diagonal de la matriz
print(M.sum()) #Suma de todos los elementos de la matriz
print(M.prod())#El producto de todos los elementos de la matriz
print(M.shape)#Tamaño de la matriz mxn
