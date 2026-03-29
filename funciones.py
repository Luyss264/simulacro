import json
import os

carpeta_data = 'data'
DATA = os.path.join(carpeta_data, 'database.json')

def crear_carpeta_si_no_existe():
    if not os.path.exists(carpeta_data):
        os.makedirs(carpeta_data)


#aqui definimos el menú
def menu():
    menuprint = """\n
    ---SISTEMA DE GESTION DE CLIENTES---
     
    1. Crear cliente
    2. Listar clientes
    3. Buscar clientes
    4. Actualizar cliente
    5. Eliminar cliente
    6. Salir
    """
    print(menuprint)

#----------FUNCIONES DE PERSISTENCIA-------------
def agregar_json(lista_clientes):
    crear_carpeta_si_no_existe()
    with open(DATA, 'w', encoding='utf-8') as archivo:
        # 'ensure_ascii=False' permite que se escriban tildes y ñ directamente
        json.dump(lista_clientes, archivo, indent=4, ensure_ascii=False)

def cargar_json(lista_clientes):
    if not os.path.exists(DATA):
        return
    try:
        with open(DATA, 'r', encoding='utf-8') as archivo:
            datos_json = json.load(archivo)
            for cliente in datos_json:
                lista_clientes.append(cliente)
    except json.JSONDecodeError:
        print("Error al leer la base de datos.")
            
#se define la función que registra los clientes 
def agregar_cliente(lista_clientes):
    
    while True:

        existe = False

        ID_cliente = input('\nAsigne un ID al cliente de 4 digitos:')
        for i in lista_clientes:
            if ID_cliente == i['ID']:
                existe=True
                break
        if existe:
            print('este cliente ya esta registrado')
        elif not ID_cliente.isdigit():
            print('Solo se admiten numeros')
        elif len(ID_cliente) != 4:
            print('Deben registrarse 4 digitos')
        else:
            break
        
    while True:
        nombre_cliente = input('\nIngrese el nombre del cliente: ').replace(" ","_").strip().lower()
        datonumero = False
        for i in nombre_cliente:
            if i.isdigit():
                datonumero = True
        
        if datonumero == True:
            print('\nNo se aceptan numeros en el nombre')
            
        else:
            break
    
    while True:
        try:
            edad_cliente = int(input('\nIngrese la edad del cliente: '))
            if edad_cliente > 12:
                break
            elif edad_cliente <= 0:
                print('\nLa edad del cliente es invalida')
            else:
                print('\nEl cliente es muy joven')
        except:
            print('\nIngrese un dato valido')
            
    while True:
        plan_cliente = input('\nIngrese el tipo de plan:\nMensual\nTrimestral\nAnual\n\n').lower().strip()
        if plan_cliente == 'mensual' or plan_cliente == 'trimestral' or plan_cliente == 'anual':
            break
        else:
            print('\nIngrese un dato valido')
            
    while True:
        estado_cliente = input('\n¿Está el cliente activo o inactivo?: ').lower().strip()
        if estado_cliente == 'activo' or estado_cliente == 'inactivo':
            break
        else:
            print('\nIngrese un dato valido')
    
    cliente = {}
    cliente['ID'] = ID_cliente
    cliente['nombre'] = nombre_cliente
    cliente['edad'] = edad_cliente
    cliente['plan'] = plan_cliente
    cliente['estado'] = estado_cliente
    
    lista_clientes.append(cliente)
    
                
def listar_clientes(lista_clientes):
    
    if len(lista_clientes) == 0:
        print('\nAún no hay clientes registrados')
    else:
        for i in lista_clientes:
            print(f'\nID:{i['ID']} | Cliente:{i['nombre']} | Edad:{i['edad']} | Plan:{i['plan']} | Estado:{i['estado']}')
        
    
        
def buscar_cliente(lista_clientes):
    
    print('\n¿Cómo desea buscar al cliente? \n1. Nombre\n2. ID')
    
    option = input('\nIngrese el número de la opción: ')
    
    if option == '1':
        nombre_search_input = input('\nIngrese el nombre del cliente:').strip().replace(" ","_").lower()
        existe = False
        for i in lista_clientes:
            if nombre_search_input == i['nombre']:
                print(f'\nID:{i['ID']} | Cliente:{i['nombre']} | Edad:{i['edad']} | Plan:{i['plan']} | Estado:{i['estado']}')
                existe = True
                break
        if not existe:
            print('Cliente no encontrado')
    
    elif option == '2':
        id_search_input = input('\nIngrese el nombre del cliente:').strip().replace(" ","_").lower()
        existe = False
        for i in lista_clientes:
            if id_search_input == i['ID']:
                print(f'\nID:{i['ID']} | Cliente:{i['nombre']} | Edad:{i['edad']} | Plan:{i['plan']} | Estado:{i['estado']}')
                existe = True
                break
        if not existe:
            print('Cliente no encontrado')
            
    else:
        print('\nOpción no valida')
        
def actualizar_cliente(lista_clientes):
    cliente_actualizar = input('\nIngrese el nombre del cliente que quiere actualizar: ').strip().replace(" ","_").lower()
    
    existe= False
    for i in lista_clientes:
        if cliente_actualizar == i['nombre']:
            existe= True
            print(f'\nVas a actualizar a: ID:{i['ID']} | Cliente:{i['nombre']} | Edad:{i['edad']} | Plan:{i['plan']} | Estado:{i['estado']}')
            print("---------")
            print('No se puede editar el ID ya que es unico')
            while True:
                nuevo_nombre_cliente = input('\nIngrese el nuevo nombre del cliente: ').replace(" ","_").strip().lower()
                datonumero = False
                for x in nuevo_nombre_cliente:
                    if x.isdigit():
                        datonumero = True
                
                if datonumero == True:
                    print('\nNo se aceptan numeros en el nombre')
                    
                else:
                    i['nombre'] = nuevo_nombre_cliente
                    break
            while True:
                try:
                    nueva_edad_cliente = int(input('\nIngrese la nueva edad del cliente'))
                    if nueva_edad_cliente > 12:
                        i['edad'] = nueva_edad_cliente
                        break
                    elif nueva_edad_cliente <= 0:
                        print('\nLa edad del cliente es invalida')
                    else:
                        print('\nEl cliente es muy joven')
                except:
                    print('\nIngrese un dato valido')
            while True:
                nuevo_plan_cliente = input('\nIngrese el tipo de plan:\nMensual\nTrimestral\nAnual').lower().strip()
                if nuevo_plan_cliente == 'mensual' or nuevo_plan_cliente == 'trimestral' or nuevo_plan_cliente == 'anual':
                    i['plan'] = nuevo_plan_cliente
                    break
                else:
                    print('\nIngrese un dato valido')
            
            while True:
                nuevo_estado_cliente = input('\n¿Está el cliente activo o inactivo?').lower().strip()
                if nuevo_estado_cliente == 'activo' or nuevo_estado_cliente == 'inactivo':
                    i['estado'] = nuevo_estado_cliente
                    break
                else:
                    print('\nIngrese un dato valido')
                    
            print(f'\nActualizaste: ID:{i['ID']} | Cliente:{i['nombre']} | Edad:{i['edad']} | Plan:{i['plan']} | Estado:{i['estado']}')
            break   
    if not existe:
        print('\nCliente no encontrado')
        
def eliminar_cliente(lista_clientes):
    
    while True:
        consultar_cliente = input('\nIngrese el ID del cliente que desea eliminar: ')
        if not consultar_cliente.isdigit(): # Simplificado: isdigit() ya hace el trabajo
            print('\nSolo se admiten números')
        elif len(consultar_cliente) != 4:
            print('\nSolo deben haber 4 dígitos')
        else:
            break
    
    cliente_encontrado = None
    
    # Buscamos el objeto cliente primero
    for i in lista_clientes:
        if i['ID'] == consultar_cliente:
            cliente_encontrado = i
            break
            
    if cliente_encontrado:
        print(f"\nSe eliminó a {cliente_encontrado['nombre']}")
        lista_clientes.remove(cliente_encontrado)
        # Importante: El archivo JSON se actualiza en el archivo principal (main) 
        # justo después de llamar a esta función, así que esto debería funcionar.
    else:
        print('\nNo se encontró el cliente')
            
            
    
    
            


