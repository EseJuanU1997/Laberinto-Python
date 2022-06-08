from array import array
import copy
import sys
import os
import time
sys.setrecursionlimit(5000)
def modo_respuesta(modo):
    respuesta = ""
    if (execute_mode == 'r'):
        respuesta = "<SOLO RESPUESTAS>"
    elif (execute_mode == 'g'):
        respuesta = "<GRÁFICO>"
    else:
        respuesta = "<No definido>"
    return respuesta
def validar_archivo2(txt_file): #DEBE VALIDAR SI ES UN LABERINTO SI ES POSIBLE
    respuesta = False
    try:
        archivo = open(txt_file)
        archivo.close
        respuesta = True
    except FileNotFoundError:
        print("No existe el archivo")
        respuesta = False
    return respuesta
def validar_archivo(file):
        try:
            with open(file) as file:
                laberinto = file.read()
        except FileNotFoundError:
            print('No existe el archivo, cargue un archivo valido')
            return ""
        # Checar si el archivo esta vacio
        if laberinto == '':
            print('Error: Archivo no valido')
        # Checar si el formato del archivo es el correcto
        # Convertir string a array 2d
        mapa = laberinto.splitlines()
        laberinto_valido = True
        # Manejo de excepcion: el texto no contiene formato de laberinto
        for r in mapa:
            if len(r) != len(mapa[0]):
                laberinto_valido = False
        # Chechar que el texto sea efectivamente un laberinto
        if(not laberinto_valido):
            print("Formato invalido, cargue otro archivo")
            return ""
        return mapa
###########################################################################################################################################
####
def returnChar(palabra):
    return [char for char in palabra]
def print_mapas(lista_mapa):
        for row in range(len(lista_mapa)):
            chained = ""
            for cell in range(len(lista_mapa[row])):
                chained+=(lista_mapa[row][cell])
            print(chained)
def limpiar_pantalla():
    os.system("clear")
    return
def explorar(x, y,caracter,caminos,mapa,counter,modo,lista_exitos):
    # Obtener informacion de la casilla del nodo actual 
    # Caso base 1: Se encontro la meta
    #caminos.append(str(x)+","+str(y))
    num_fracasos = 0
    cadena_s = ""
    caminos += "("+str(x)+","+str(y)+")->"
    mapa_s = []
    counter_s = 0 #counter saved
    counter_r = 0 #counter recieved
    counter += 1  #incremento de movimientos
    mapas = []
    #print("Direccion actual (X,Y): "+str(x)+","+str(y))
    if(caracter != 'E'):
        mapa[y][x] = caracter
    if(modo == "g"):
        print_mapas(mapa)
        os.system("clear")
    mapas = copy.deepcopy(mapa)  
    backUp = copy.deepcopy(mapas) #copia del mapa que requiero para saber en que posición regreso
    mapa = []                     #limpio mapa para que reciba un nuevo valor de la recursividad
    encontro_camino = False
    flagExito = False
##validaciones por caso
    if mapas[y][x - 1] == ' ':
        encontro_camino = True
        mapa,counter_r,cadena_r,num_fracasos_r = explorar(x-1,y,'$',caminos,copy.deepcopy(mapas),counter,modo,lista_exitos)
        if(cadena_r != ""):
                if(counter_s == 0 and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
                if (counter_s > counter_r and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
        num_fracasos += num_fracasos_r
        num_fracasos_r = 0
        #print("LEFT Current data in counter: "+str(counter)+" Current data in Counter_s: "+str(counter_s))
        mapas = copy.deepcopy(backUp)
        cadena_r = ""
        mapa = []
    if mapas[y][x + 1] == ' ':
        encontro_camino = True
        mapa,counter_r,cadena_r,num_fracasos_r  = explorar(x+1,y,"$",caminos,copy.deepcopy(mapas),counter,modo,lista_exitos)
        if(cadena_r != ""):
                if(counter_s == 0 and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
                if (counter_s > counter_r and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
        num_fracasos += num_fracasos_r
        num_fracasos_r = 0
        #print("RIGHT Current data in counter: "+str(counter)+" Current data in Counter_s: "+str(counter_s))
        mapas = copy.deepcopy(backUp)
        cadena_r = ""
        mapa = []
    if mapas[y + 1][x] == ' ':
        encontro_camino = True
        mapa,counter_r,cadena_r,num_fracasos_r  = explorar(x,y+1,"$",caminos,copy.deepcopy(mapas),counter,modo,lista_exitos)
        if(cadena_r != ""):
                if(counter_s == 0 and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
                if (counter_s > counter_r and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
        num_fracasos += num_fracasos_r
        num_fracasos_r = 0
        #print("DOWN Current data in counter: "+str(counter)+" Current data in Counter_s: "+str(counter_s))
        mapas = copy.deepcopy(backUp)
        cadena_r = ""
        mapa = []
    if mapas[y - 1][x] == ' ':
        encontro_camino = True
        mapa,counter_r,cadena_r,num_fracasos_r = explorar(x,y-1,"$",caminos,copy.deepcopy(mapas),counter,modo,lista_exitos)
        if(cadena_r != ""):
                if(counter_s == 0 and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
                if (counter_s > counter_r and counter_r != 0):
                    mapa_s = copy.deepcopy(mapa)
                    counter_s = (counter_r)
                    cadena_s = (cadena_r)
        num_fracasos += num_fracasos_r
        num_fracasos_r = 0
        mapas = copy.deepcopy(backUp)
        cadena_r = ""
        mapa = []
        ### si encontró @
    if mapas[y][x - 1] == '@':
        counter+=1
        caminos+="SALIDA: "+str(counter)
        flagExito = True
    elif mapas[y][x + 1] == '@':
        counter+=1
        caminos+="SALIDA: "+str(counter)
        flagExito = True
    elif mapas[y + 1][x] == '@':
        counter+=1
        caminos+="SALIDA: "+str(counter)
        flagExito = True
    elif mapas[y - 1][x] == '@':
        counter+=1
        caminos+="SALIDA: "+str(counter)
        flagExito = True
    if(flagExito): #SI ENCONTRÓ LA SALIDA (TRUE)
        if(modo == "g"):
            print_mapas(mapas)
            print(str(caminos))
            os.system("clear")
        lista_exitos.append(caminos)
        if(modo == "r"):
            print("Camino encontrado: "+str(len(lista_exitos))+" con "+str(counter)+" movimientos")
        return copy.deepcopy(mapas),counter,caminos,0
    if(not encontro_camino): #ENTRO EN UNA RAMIFICACIÓN (TRUE)
        return copy.deepcopy(mapa_s),counter_s,cadena_s,1
    return copy.deepcopy(mapa_s),counter_s,cadena_s,num_fracasos
#################################
        #input("PRESS ENTER TO CONTINUE")
###################################
def ejecutar_opciones(txt,modo): #INICIA EL MODULO PARA RESOLVER EL PROBLEMA
    mapa = validar_archivo(txt)
    # Encontrar Origen
    x = []
    y = []
    mapa_s = []
    counter_s = []
    cadena_s = []
    lista_exitos = list()
    num_fracaso = 0
    for j in range(len(mapa[0])):
        if mapa[0][j] == 'E':
            x = j
            y = 0
            break
    caminos = ""
    termino = 0
    label = ""
    arrayMap = [returnChar(sentence)  for sentence in mapa]
                                                #x,y,caracter,caminos,mapa,counter,flagLeft,flagDown,flagRight,flagUp,modo,start
    mapa_s,counter_s,cadena_s,num_fracasos = explorar(x,y,'E',caminos,arrayMap,termino,modo,lista_exitos)
    if(cadena_s != ""):
        print_mapas(mapa_s)
        print("Esta es la mejor salida (con "+str(counter_s)+" movimientos) entre "+str(len(lista_exitos))+" soluciones posibles.")
        print("Fracasos: "+str(num_fracasos))
        print("Camino recorrido: ")
        print(cadena_s)
        #if(modo == "r"):
        #    k = input("deseas mostrar las demas soluciones? \n1) SI\nCualquier otra cosa NO\nRespuesta: ")
        #    if(k == "1"):
        #        for i in range(len(lista_exitos)):
        #            print(lista_exitos(i))
    return "3"
#############################################################################################################################################
#variables iniciales:

archivo_cargado = False
label_inicio = ""
execute_mode = "0" #0 sin elección, g modo grafico, r solo resultados, cualquiera equis sera igualado a 0.
opc_elegida = "1"
laberinto_txt = ""
#fin variables
if len(sys.argv) == 3:
    execute_mode = sys.argv[1]
    if(validar_archivo(str(sys.argv[2])) != ""):
        laberinto_txt = str(sys.argv[2])
    else:
        print("Laberinto no valido")
        laberinto_txt = "<No cargado aún>"
    archivo_cargado = True
    print("LABERINTO: "+sys.argv[2])
if len(sys.argv) == 2:
    execute_mode = str(sys.argv[1])
    laberinto_txt = "<No cargado aún>"
if len(sys.argv) == 1:
    laberinto_txt = "<No cargado aún>"
    execute_mode = "0"
#labels informativos
label_loaded = "EL archivo ha sido cargado con exito, verificando si es un laberinto válido\n"
label_verify = "El laberinto es válido, empezando a iterar\n"
label_menu = "MENU INICIAL - LABERINTO - :\n1) CARGAR ARCHIVO\n2) ELEGIR MODO DE EJECUCIÓN\n3) ENCONTRAR RESPUESTAS\n-Salir con cualquier input no indicado-"
#fin_labels
while (opc_elegida == "1" or opc_elegida == "2" or opc_elegida == "3"):
    limpiar_pantalla()
    label_inicio = "Bienvenido al laberinto iterador\n"+"Nombre archivo: "+laberinto_txt+"\nMODO: "+modo_respuesta(execute_mode)
    print(label_inicio)
    print("\n"+label_menu)
    opc_elegida = input("Ingrese opción: ")
    if (opc_elegida == "1"):
        laberinto_txt = input("Defina el nombre del archivo\nEjemplo: ejemplo1.txt\nARCHIVO: ")
        if(validar_archivo(laberinto_txt) != ""):
            print("Cargado con exito el archivo: "+laberinto_txt+"\n")
            archivo_cargado = True
        else:
            laberinto_txt = "<No cargado aún>"
            print("Archivo no existente")
            archivo_cargado = False
    if (opc_elegida == "2"):
        execute_mode = input("MODOS DISPONIBLES\ng) GRAFICO\nr) RESPUESTA\n")
        if not(str(execute_mode) == "r" or str(execute_mode == "g")):
            execute_mode = "0"
            print("Modo no valido, intente de nuevo\n")
    
    
    
    if (opc_elegida == "3"):
        validacion = True
        texto_error = "########################################"
        print("VALIDANDO INFORMACIÓN REQUERIDA")
        if(not archivo_cargado):
            texto_error+="\nPor favor, elige un archivo valido"
            validacion = False
        if not(str(execute_mode) == "r" or str(execute_mode) == "g"):
            texto_error+="\nPor favor, elige un modo valido"
            validacion = False
        if(validacion):
            print("EJECUTANDO...")
            time_inicio = time.time()
            opc_elegida = ejecutar_opciones(laberinto_txt,execute_mode)
            time_fin = time.time()
            print("Tiempo de ejecución: "+str(time_fin - time_inicio)+" segundos")
            print("¿Deseas probar otro laberinto? (1-3) CONTINUAR - [Any key] SALIR")
            opc_elegida = input("Respuesta: ")
        else:
            texto_error+="\n########################################"
            print(texto_error)