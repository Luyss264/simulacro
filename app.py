from funciones import *

lista_clientes = []

cargar_json(lista_clientes)
option = ''
while option != '6':
    menu()
    option = input('\nSeleccione el número de la opción que desea: ')
    
    if option == '1':
        agregar_cliente(lista_clientes)
        agregar_json(lista_clientes)
        
    elif option == '2':
        listar_clientes(lista_clientes)
        
    elif option == '3':
        buscar_cliente(lista_clientes)
    
    elif option == '4':
        actualizar_cliente(lista_clientes)
    
    elif option == '5':
        eliminar_cliente(lista_clientes)
    
    elif option == '6':
        print('\nAdiós\n')
    
    else:
        print('\nLa opción no es valida')
    