edad=int(input('Introduce tu edad: '))

veintes=edad>=20 and edad<=30
print(veintes)
treintas=edad>=30 and edad<=40
print(treintas)

if veintes or treintas:
#    print('Eres un adulto joven')
        if veintes:
            print('Eres un adulto joven (en sus veintes)')
        elif treintas:
            print('Eres un adulto joven (en sus treintas)')
        else:
            print('Fuera de rango')
else:
    print('No eres un adulto joven')