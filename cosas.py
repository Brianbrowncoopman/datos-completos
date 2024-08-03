from datetime import datetime

print("=======================")
print("Ingresa tus datos")
print("=======================")

# Solicitar entradas del usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu direccion: ")
estado_civil = input("Tu estado civil (casado o soltero): ")

# Obtener el año actual
año_actual = datetime.now().year

# Inicializar variables opcionales
nombre_pareja = ""
años_de_relacion = ""
año_matrimonio = ""

if estado_civil.lower() == "casado":
    nombre_pareja = input("Ingresa el nombre de tu pareja: ")
    años_de_relacion = int(input("Ingresa los años de relacion: "))
    año_matrimonio = año_actual - años_de_relacion

# Información de hijos
hijos = input("¿Tienes hijos? (si o no): ").lower()
hijos_info = []
if hijos == "si":
    cantidad_hijos = int(input("Ingresa cuántos hijos: "))
    for i in range(cantidad_hijos):
        genero_hijo = input("Es hombre o mujer: ").lower()
        nombre_hijo = input("Ingresa su nombre: ")
        años_hijo = int(input("¿Cuántos años tiene?: "))
        año_nacimiento_hijo = año_actual - años_hijo
        if genero_hijo == "hombre":
            hijos_info.append(f"hijo llamado {nombre_hijo} nacido en {año_nacimiento_hijo} con {años_hijo} años")
        elif genero_hijo == "mujer":
            hijos_info.append(f"hija llamada {nombre_hijo} nacida en {año_nacimiento_hijo} con {años_hijo} años")

# Construir la cadena de datos completos
datos_completos = f"Tu nombre es {nombre}, tu apellido es {apellido}, tu edad es {edad}, vives en {direccion}, actualmente estás {estado_civil}."
if estado_civil.lower() == "casado":
    datos_completos += f" El nombre de tu pareja es {nombre_pareja} y tienes una relación de {años_de_relacion} años. Se casaron en el año {año_matrimonio}."

if hijos == "si":
    datos_completos += f" Tienes {cantidad_hijos} hijos: " + ", ".join(hijos_info) + "."

print(datos_completos)
