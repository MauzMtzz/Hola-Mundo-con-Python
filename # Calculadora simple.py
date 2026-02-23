# Calculadora simple

print("=== Calculadora Básica ===")

# Pedimos los números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Pedimos la operación
operacion = input("Elige la operación (+, -, *, /): ")

# Realizamos la operación
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir entre cero"
else:
    resultado = "Operación no válida"

# Mostramos el resultado
print("Resultado:", resultado)