valor=int(input('Escribe el valor: '))
valorMinimo=0
valorMaximo=5

dentroRango=valor>=valorMinimo and valor<=valorMaximo

if dentroRango:
    print(f'El valor {valor} se encuentra dentro del rango.')
else:
    print(f'El valor {valor} se encuentra fuera del rango')