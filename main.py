# bloco iniciado por lui richard
import sqlite3
from system import start, menu, invalid_option

start()

option = 0
driver = 0
vehicles = 0
routes = 0

while (option!=3):
    menu()
    option = int(input("Digite o número da opção que deseja: "))
    if (option == 1):
        print("\n[ 1 ] Cadastrar motorista")
        print("[ 2 ] Visualizar motoristas cadastrados")
        print("[ 3 ] Editar motorista")
        print("[ 4 ] Remover motorista")
        print("[ 5 ] Voltar ao menu principal\n")

        driver = int(input("Digite o número da opção que deseja: "))

        if (driver == 1):
            register_driver()
            print("")

        elif (driver == 2):
            read_driver()
            print("")

        elif (driver == 3):
            update_driver()
            print("")

        elif (driver == 4):
            remove_driver()
            print("")

        elif (driver == 5):
            menu()
            print("")

        else:
            invalid_option()
    
    if (option == 2):
        print("\n[ 1 ] Cadastrar veículos")
        print("[ 2 ] Visualizar veículos cadastrados")
        print("[ 3 ] Editar veículos")
        print("[ 4 ] Remover veículos")
        print("[ 5 ] Voltar ao menu principal\n")

        vehicles = int(input("Digite o número da opção que deseja: "))

        if (vehicles == 1):
            register_vehicles()
            print("")

        elif (vehicles == 2):
            read_vehicles()
            print("")

        elif (vehicles == 3):
            update_vehicles()
            print("")

        elif (vehicles == 4):
            remove_vehicles()
            print("")

        elif (vehicles == 5):
            menu()
            print("")

        else:
            invalid_option()

    if (option == 3):
        print("\n[ 1 ] Cadastrar rotas")
        print("[ 2 ] Visualizar rotas cadastrados")
        print("[ 3 ] Editar rotas")
        print("[ 4 ] Remover rotas")
        print("[ 5 ] Voltar ao menu principal\n")

        routes = int(input("Digite o número da opção que deseja: "))

        if (routes == 1):
            register_routes()
            print("")

        elif (routes == 2):
            read_routes()
            print("")

        elif (routes == 3):
            update_routes()
            print("")

        elif (routes == 4):
            remove_routes()
            print("")

        elif (routes == 5):
            menu()
            print("")

        else:
            invalid_option()

# bloco fechado por lui richard