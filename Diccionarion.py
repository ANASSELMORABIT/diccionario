# #  TAREA 2
# # A-
def doblar(numero):
    return numero*2
NUMEROS=[1,2,3,4,5,6,7]
map(doblar,NUMEROS)
NUMERO_DOBLAR=list(map(doblar,NUMEROS))
print(NUMERO_DOBLAR)
# #B-
def mayuscula(palabra):
    return palabra.upper()
PALABRAS=["garza","urraca","gorríon","petirrojo"]
PALABRAS_MAYUSCULAS=list(map(mayuscula,PALABRAS))
print(PALABRAS_MAYUSCULAS)
# TAREA 3:
#A:
def constractura_Tupla(lista):
    Tupla=tuple(lista)
    return Tupla
# #B
def constractura_lista(Tupla):
    lista=list(Tupla)
    return lista
lista1=[1,2]
lista2=[3,4]
lista3=[5,6]
X=(lista1,lista2,lista3)
print(X)
Y=constractura_lista(X)
print(Y)
Y[0][0]=7
print(Y)
X=constractura_Tupla(Y)
print(X)
#Tarea 4
cola_pedidos = ["pedido345671","pedido628316","pedido235252"]  
def procesarPedido(cola_pedidos):
    print(f"Procesar {cola_pedidos[0]}")
    return
def encolarPedido(cola_pedidos,pedido):
    return cola_pedidos.append(pedido)
print(cola_pedidos)
encolarPedido( cola_pedidos,"pedido123")
print(cola_pedidos)
def vaciarcola(lista):
    for i in range(0,len(lista)):
        lista.pop(0)
    return lista
#TAREA 5
dicc_perifijos=dict(BARCELONA=93,MADRID=91,SEVILLA=955,MALAGA=952,GRANADA=958,ALICANTE=965)
for X,Y in dicc_perifijos.items():
    print(f"{X} : {Y}")

def Mostrar_Perifijos():
    while True:
        ciudad=input("introduzir una ciudad:").upper()
        i=0
        for X in dicc_perifijos.keys():
            if X==ciudad:
                i=i+1
        if i!=0:
            print(f"El perifijo de este ciudad es :{dicc_perifijos.get(ciudad)}")
            break
def Add_Perfijos():
    while True:
        ciudad_new=input("introduzir una ciudad nueva:").upper()
        Perifijo=int(input("introduxir el perifijo de este ciudad:"))
        i=0
        for X,Y in dicc_perifijos.items():
            if (X==ciudad_new or Y==Perifijo):
                i=i+1
        if i==0:
            dicc_perifijos[ciudad_new]=Perifijo
            print("El nuevo Diccionario:")
            for X,Y in dicc_perifijos.items():
                print(f"{X} : {Y}")
            break
        else:
            print("Eligir una ciudad y un perifijo que no existen en la lista")
print("-Para mirar un perifijo de una ciudad (A).\n-Para Añadir una ciudad y un perifijo nuevos(B).\n-Para salir (C)")
while True:
    opcion=input("Eligir una opción:").upper()
    if (opcion=="A"):
        Mostrar_Perifijos()
    elif (opcion=="B"):
        Add_Perfijos()
    else:
        break
#Tarea 6
Cadena_Texto=input("ingrasa una caden de texto:")
lista_Cadena=Cadena_Texto.split()
print(lista_Cadena)
dicc_Cadena=dict()
for palabra in lista_Cadena:
        i=0
        if palabra not in dicc_Cadena.keys():
                for Y in lista_Cadena:
                        if palabra==Y:
                                i=i+1
                dicc_Cadena[palabra]=i
print(dicc_Cadena)