print('Proporcione los siguientes datos del libro.')

nombre=(input('Proporcione el nombre: '))

id=int(input('Proporciona el ID del libro: '))

precio=float(input('Proporciona el precio del libro: '))

envíoGratis=input('Indica si el envío en gratis (True/False): ')

if envíoGratis=='True':
    envíoGratis=True
elif envíoGratis=='False':
    envíoGratis=False

else:
    envíoGratis='Valor incorrecto, por favor ingresa True o False'

print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    ¿Envío gratis?: {envíoGratis}
''')