#Se importan las librerias
import random

#Genera 100 datos aleatorios entre 0 y 1 para dos eventos independientes A y B
n = 100
A = [random.randint(0, 1) for _ in range(n)]
B = [random.randint(0, 1) for _ in range(n)]

#Calcula la frecuencia de los eventos A, B, $A\cap B$ y $A\cup B$
fA = A.count(1) #Se cuentan las veces que el evento A tuvo 1s
fB = B.count(1) #Se cuentan las veces que el evento B tuvo 1s
fAintB = sum([1 for a, b in zip(A, B) if a == 1 and b == 1]) #Se cuentan las veces cuando el evento A y el evento B son 1
fAuB = sum([1 for a, b in zip(A, B) if a == 1 or b == 1]) #Se cuentan las veces cuando el evento A o el evento B son 1
#Calcula las probabilidades
pA = fA / n #Probabilidad del evento A
pB = fB / n #Probabilidad del evento B
pAintB = fAintB / len(A) #Probabilidad del evento A interseccion B
pAuB = fAuB / len(A) #Probabilidad del evento A interseccion B

print("P(A)=", pA)
print("P(B)=", pB)
print("P(A ∩ B)=",pAintB)
print("P(A ∪ B)=",pAuB)

#Prueba $P(A \cup B)=P(A)+P(B)-P(A \cap B)$

# Aplicando la ecuacion P(A ∪ B)
pAUB = pA + pB - pAintB
print("P(A ∪ B)=",pAUB)

Prueba $P(A \cap B)=P(A)P(B)$

pAintB1=pA*pB
print("P(A ∩ B)=",pAintB1)

#De esta manera ambos resultados son similares, comprobando que estas ecuaciones son ciertas
