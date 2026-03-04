#vacaciones=True
#diaDescanso=False

#if vacaciones or diaDescanso:
#    print("Puede ir al partido de Fútbol")
#else:
#    print("Tiene obligaciones que cumplir")

vacaciones=False
diaDescanso=False

if not (vacaciones or diaDescanso):
    print("Tiene obligaciones que cumplir")
else:
    print("Puede ir al partido de Fútbol")