import math
Initial_height = float(input ("¿A que altura sobre el suelo se sitúa el objeto? "))

Gravity = float(input("¿Cual es la gravedad en la superficie del cuerpo al que se espera que caiga el objeto? "))
#Redundante
Opcion_planeta = input("¿En que planteta estás (Tierra, Marte, Luna, Jupiter, Sol)")
Tiempo = float(input("¿Tras cuantos segundos después de la caída quieres calcular la altura del objeto? "))
Masa_objeto = float(input("¿Cual es la masa del objeto? "))
Diametro_objeto = float(input("¿Cual es el diámetro del objeto?"))

#Diccionario gravedades
GRAVEDADES = {
    "Tierra": 9.81,
    "Marte": 3.7,
    "Luna":1.62,
    "Jupiter": 24.79,
    "Sol": 274
    }

if Opcion_planeta in GRAVEDADES:
    Gravity = GRAVEDADES[Opcion_planeta]
else:
    print("Debes introducir un planeta de la lista, si no, introduce la gravedad en la superficie que desees. ")
    Gravity = Gravity

Opcion_planeta = Opcion_planeta.lower()

Velocidad_terminal = float((((8*Masa_objeto*Gravity)/((1.2*0.47*3.141592* (Diametro_objeto))**2)))**0.5)
Altura_tiempo = float(Initial_height-((Velocidad_terminal**2)/Gravity)*math.log(math.cosh((Gravity*Tiempo)/Velocidad_terminal)))
Velocidad_llegada = float((Velocidad_terminal*math.tanh((Gravity*Tiempo)/Velocidad_terminal)))
Tiempo_hasta_suelo = float((Velocidad_terminal/Gravity)*math.acosh(math.exp((Gravity*Initial_height/(Velocidad_terminal**2)))))


if Altura_tiempo <=0:
    print(Tiempo_hasta_suelo)
    print(Velocidad_llegada)
    print(0)
#elif redundante por corrección de tanh
elif Velocidad_llegada >= Velocidad_terminal:
    print(Tiempo_hasta_suelo)
    print(Velocidad_terminal)
    print(Altura_tiempo)
else:

    print(Tiempo_hasta_suelo)
    print(Velocidad_llegada)
    print(Altura_tiempo)