# TALLER 1 PYTHON
# AUTOR(A): JUAN CAMILO PEREZ GOMEZ
# FECHA:7 OCTUBRE 2022
from datetime import datetime
fechacompleta=datetime.now()	#flecha actual
hora=fechacompleta.time()
fecha=fechacompleta.date()
nombre=input('Digite su nombre:')
print("Bienvenido",nombre.title())
print("Fecha de ejecucion del programa", fecha)
print("Hora de ejecucion del programa", hora)
n1=int(input("digite el primer número: "))
n2=int(input("digite el segundo número: "))
n3=int(input("digite el tercer número: "))
suma=n1+n2+n3
resta=n1-n2-n3
producto=n1*n2*n3
division=n1/n2 
print("La adicion de los tres números es: ",suma)
print("La resta de los tres números es: ", resta)
print("La multiplicacion de los tres números es := ", producto) 
print("La división de los primeros dos números es: = ", division) 
print("TERMINO LA EJECUCION DEL PROGRAMA ")
