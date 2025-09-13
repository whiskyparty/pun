base = float(input("ingresa la base"))
altura = float(input("ingresa la altura:"))
area = base * altura / 2
print("el area del triangulo es:", area)


celsius = float(input("ingrese la temperatura en celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("{celsius} grados celsius son {farenheit} grados fahrenheit")

nombre = input("ingresa tu nombre:")
apellido = input("ingresa tu apellido:")
nombre_completo = nombre+ "" + apellido
print("tu nombre completo es:{nombre complto}")

numero = int(input("ingresa un numero:"))
if numero % 2 == 0:
    print(f"el numero{numero}es par")
else:
    print(f"el numero{numero}es impar")


edad = int(input("ingresa tu edad:"))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("no eres mayor de edad")

num1 = float(input("ingresa el primer numero:"))
num2 = float(input("ingresa el segundo numero:"))
if num1 > num2:
    print(f"{num1}es meyor que{num2}")
elif num1 > num2:
    print(f"{num1}es mayor que{num2}")
else:
    print(f"{num1}es igual que{num2}")

numero = int(input("ingresa un numero:"))
if numero >= 10 and numero <= 20:
    print(f"el numero{numero}esta entre 10 y 20")
else:
    print(f"el numero{numero}no esta entre 10 y 20")

password = input("ingresa la contrasena:")
if password == "panty123":
    print("contrasena correcta")
else:
    print("contrasena incorrecta")

precio_mercancia = float(input("ingresa el precio de la mercancia:"))
if precio_mercancia >100:
    descuento = precio_mercancia * 0.15
    precio_final = precio_mercancia - descuento
    print(f"el precio final con descuento es:{precio_final}")
else:
    print(f"el precion final sin descuento es:{precio_mercancia}")

numero = float(input("ingresa un numero:"))
if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")

year = int(input("ingresa un ano:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"el ano es bisiesto")
else:
    print(f"el ano no es bisiesto")

nota = float(input("ingresa la nota(0-100):"))
if 90 <=nota <= 100:
    print("tu calificacion es A")
elif 80<= nota <90:
    print("tu calificacion es B")
else:
    print("tu calificacion es c")

letra = input("ingresa una letra:").lower()
if letra in "aeiou":
    print(f"{letra} es una vocal")
else: 
    print(f"{letra} no es una vocal")

print("elige una opcion:")
print("1. saludar")
print("2. despedirte")
print("3. dar un cumplido")
opcion = input("ingresa tu eleccion (1,,2,3):")
if opcion == "1":
    print("hola como estas?")
elif opcion == "2":
    print("hasta luego! que tengas buen dia")
elif opcion == "3":
    print("eres genial!")
else:
    print("opcion no valida")


lado1 = float(input("ingrsa la longitud del lado 1:"))
lado2 = float(input("ingresa la longitud del lado 2:"))
lado3 = float(input("ingresa la longitud del lado 3:"))
if lado1 == lado2 and lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")
        









                




    





