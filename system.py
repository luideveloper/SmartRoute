# bloco iniciado por lui richard

import sqlite3
import time
from driver import register_driver, read_driver, update_driver, remove_driver
from vehicles import register_vehicles, read_vehicles, update_vehicles, remove_vehicles

def start():
    con = sqlite3.connect('SmartRoute/dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (codigo integer, marca VARCHAR(200), modelo VARCHAR(200), data_fabricação VARCHAR(200), km_atual VARCHAR(200), ultima_km_manutencao VARCHAR(200));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    con.commit()
    con.close()

def first_menu():
    print("\nOlá, seja bem vindo ao Smart Route, o que você deseja?\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas\n")

def check():
    registered_user = "lui"
    registered_password = "123"
    
    user = input("\nDigite seu usuário: ")
    password = input("Digite sua senha: ")
    if (user == registered_user and password == registered_password):
        register_driver()
        print("")
    else:
        post_check_menu()

def post_check_menu():
    print("\n> Usuário ou senha errado")
    time.sleep(2)
    print("\nDeseja tentar novamente?\n")
    print("[ 1 ] sim")
    print("[ 2 ] não")
    option = int(input("\nO que você deseja? "))
    if (option == 1):
        check()
    elif (option == 2):
        full_menu()

def full_menu():

    option = 0
    driver = 0
    vehicles = 0
    routes = 0

    while (option!=3):
        first_menu()
        option = int(input("Digite o número da opção que deseja: "))
        if (option == 1):
            print("\n[ 1 ] Cadastrar motorista")
            print("[ 2 ] Visualizar motoristas cadastrados")
            print("[ 3 ] Editar motorista")
            print("[ 4 ] Remover motorista")
            print("[ 5 ] Voltar ao menu principal\n")

            driver = int(input("Digite o número da opção que deseja: "))

            if (driver == 1):
                check()

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
                first_menu()
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
                first_menu()
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
                first_menu()
                print("")

            else:
                invalid_option()

def invalid_option():
     print("Você digitou uma opção inválida")

# bloco fechado por lui richard