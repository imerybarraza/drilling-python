nombres = ["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]
newlist = nombres[:]
magos = ["Harry Houdini","David Blaine","Teller"]
copia_magos= magos[:]
cientificos=["Newton","Hawking","Einstein"]
otros = []

def imprimir_nombres():
    print("-----Lista de Nombres-----\n")
    for i in newlist:
        print(i)
        

def hacer_grandioso():
    for index,mago in enumerate(copia_magos):
        copia_magos[index]= f"El gran {mago}"
    return copia_magos
       

def lista_otros():
    for i in newlist:
        if i not in cientificos and i not in magos:
            otros.append(i)
    return otros

def imprime_todos():
    for i,j,k in zip(cientificos,magos,otros):print(f"Cientificos {i}, ---- Magos {j}, ---- Otros ---- {k}")

lista_nombres = imprimir_nombres()
print("-------------Hacer grandiosos-------------------\n")
grandioso = hacer_grandioso()
print(grandioso,"\n")
print("-------------Lista otros-------------------------\n")
print(lista_otros(),"\n")
print("-------------Imprimir todos recorriendo las 3 listas-------------------------\n")
lista_todos = imprime_todos()
