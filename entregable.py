# problema 1 
print("me diras 4 numeros para sacar promedio")
promedio=0
for i in range(4):
    i=int(input())
    promedio += i
resultado = promedio/4
print(resultado)

#problema 2
persona_1= 2000
persona_2= 5000
persona_3= 3500
total =persona_1+persona_2+persona_3
print("Inversion total es de",total)
print("\n porcentaje de cada perosona \n")
print("porcentaje de inversion de la persona 1 es de",int((persona_1/total)*100),'%')
print("porcentaje de inversion de la persona 2 es de",int((persona_2/total)*100),'%')
print("porcentaje de inversion de la persona 3 es de",int((persona_3/total)*100),'%')

#problema 3
nombre = input("Nombre: ")
horas = int(input('Horas de trabajo:'))
salario_hora = int(input('El salario por hora: '))
sueldo = horas*salario_hora
print(nombre,", tu sueldo es de",(sueldo*115)/100)

#problema 4
print("\n OPCIONES A REALIZAR \n")
print("Precione 1 para sumar")
print("Precione 2 para restar")
print("Precione 3 para multiplicar")
print("Precione 4 para dividir")
opcion= int(input("¿Que opcion desea? "))
x=int(input("Primer numero: "))
y=int(input("Segundo numero: "))

if opcion==1:
    print("Elijio 'SUMA', y la respuesta es: ",x+y)
    
elif opcion==2:
    print("Elijio 'RESTA', y la respuesta es: ",x-y)
elif opcion==3:
    print("Elijio 'MULTIPLICAR', y la respuesta es: ",x*y)
elif opcion==4:
    print("Elijio 'DIVIDIR', y la respuesta es: ",x/y)
else:
    print("Opcion erronea")

#problema 5 si quiere verificar reemplaze los numeros que estan al final del def
print("\n Que numero es mayor \n")
def numero_mayor(a,b,c):
    if a>b and a >c:
        print(a,"es mayor que todos")
    elif b>a and b>c:
        print(b,"es mayor que todos")
    elif c>a and c>b:
        print(c,"es mayor que todos")
numero_mayor(11,5,8)

#problema 6
print("\n Determina si un numero es par o impar \n")
x=int(input("Dime que numero deseas introducir: "))
if x % 2==0:
    print(x,"es par")
else:
    print(x,"es impar")

#problema 7

def area_triangulo(base,altura):
    return (base*altura)/2
a  = int(input("BASE: "))
b = int(input("ALTURA: "))
resultado=area_triangulo(a,b)
print(resultado)

#problema 8
dni= input("Ingrese el DNI: ")
if len(dni) == 8:
    print("La cantidad de digitos es correcto")
else:
    print("La cantidad de digitos no es correcto")

#problema 9
venta={
    "salsa":56.00,
    "rock":63.00,
    "pop":87.00,
    "folclore":120.50
}
print(venta)
print("\nSi llevas discos Pop o Rock, accedes a un Poster gratis por la compra de 6 unidades a más de un mismo genero musical.\n")

disco=input("Disco que comprara: ")
cantidad=int(input("¿Cuantos discos llevara? "))
pago=cantidad*venta.get(disco)
poster = "Accedes al poster de regalo del grupo 'LOS SULTANES'"
def sin_Poster(disco,cantidad):
    if disco=="salsa" or disco=="folclore":
        if cantidad>=1 and cantidad<=3:
            print("El importe a pagar es de",pago,", y no accede a Poster.")
        elif cantidad==4:
            pago2=(pago*94)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 6.0%, ahora el importe a pagar es de {pago2}")
            print("*No accede a Poster")
        elif cantidad>=5 and cantidad<=10 :
            pago2=(pago*92)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 8.0%, ahora el importe a pagar es de {pago2}")
            print("*No accede a Poster")
        elif cantidad>=11 :
            pago2=(pago*89.8)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 10.2%, ahora el importe a pagar es de {pago2}")
            print("*No accede a Poster")
def Poster(disco,cantidad):
    if disco=="pop" or disco=="rock":
        if cantidad>=1 and cantidad<=3:
            print("El importe a pagar es de",pago,", y no accede a descuento.")
            print("*No accede a Poster")
        elif cantidad==4:
            pago2=(pago*94)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 6.0%, ahora el importe a pagar es de {pago2}")
            print("*No accede a Poster")
        elif cantidad ==5:
            pago2=(pago*92)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 8.0%, ahora el importe a pagar es de {pago2}")
            print("*No accede a Poster")
        elif cantidad>=6 and cantidad<=10 :
            pago2=(pago*92)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 8.0%, ahora el importe a pagar es de {pago2},ademas {poster}")
        elif cantidad>=11 :
            pago2=(pago*89.8)/100
            print(f"El importe de compra es de {pago} y accede a un descuento del 10.2%, ahora el importe a pagar es de {pago2},ademas {poster}")

sin_Poster(disco,cantidad)
Poster(disco,cantidad)           

#problema 10
pago_dia ={"mañana":37,"tarde":38.20,"noche":38.50}

horas = int(input("¿Cuantas horas trabajas? "))
turno = input("¿En que turno trabaja? ")
salario = horas*pago_dia.get(turno)
 
if turno=="mañana" or turno=="tarde":
    print("El salario neto es de",salario)
elif turno=="noche":
    if salario>=2000 and salario<=5000:
        print("El salario neto es de",(salario*85)/100)
    elif salario>=8000 and salario<= 10000:
        print("El salario neto es de",(salario*83)/100)
else:
    pass