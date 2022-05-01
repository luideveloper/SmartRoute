# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time
from accounts import creat_account, recovery_account, post_error_recovery_account, remove_account
from driver import register_driver, read_driver, update_driver, remove_driver
from vehicles import register_vehicles, read_vehicles, update_vehicles, remove_vehicles

def start():
    con = sqlite3.connect('SmartRoute/dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (codigo integer, marca VARCHAR(200), modelo VARCHAR(200), data_fabricação VARCHAR(200), km_atual VARCHAR(200), ultima_km_manutencao VARCHAR(200));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id integer not null, user VARCHAR(200), password VARCHAR(200), security_key VARCHAR(100), PRIMARY KEY (id));")
    con.commit()
    con.close()

def first_menu():
    print("\nOlá, seja bem vindo ao Smart Route, o que você deseja?\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa\n")

def check():
    con = sqlite3.connect("SmartRoute/dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT user, password FROM accounts;"
    cursor.execute(cod_query_read)

    for linha in cursor.fetchall():
        user_bd = linha[0]
        password_bd = user_bd = linha[1]
        user = input("\nDigite seu usuário: ")
        password = input("Digite sua senha: ")
        if (user == user_bd and password == password_bd):
            register_driver()
            print("")
        else:
            post_check_menu()

def post_check_menu():
    print("\n> Usuário ou senha errado")
    time.sleep(2)
    print("\nEscolha uma das opções\n")
    print("[ 1 ] Tentar novamente")
    print("[ 2 ] Recuperar senha")
    print("[ 3 ] Voltar ao menu principal")
    print("[ 4 ] Sair do sistema")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        check()
    elif (option == 2):
        recovery_account()
    elif (option == 3):
        full_menu()
    elif (option == 4):
        exit()
    else:
        invalid_option()

def full_menu():

    option = 0
    driver = 0
    vehicles = 0
    routes = 0
    accounts = 0

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

        if (option == 4):
            print("\n[ 1 ] Cadastrar conta")
            print("[ 2 ] Recuperar conta")
            print("[ 3 ] Visualizar relatório")
            print("[ 4 ] Excluir contas")
            print("[ 5 ] Voltar ao menu principal\n")

            routes = int(input("Digite o número da opção que deseja: "))

            if (routes == 1):
                creat_account()
                print("")

            elif (routes == 2):
                recovery_account()
                print("")

            elif (routes == 3):
                update_routes()
                print("")

            elif (routes == 4):
                remove_account()
                print("")

            elif (routes == 5):
                first_menu()
                print("")

            else:
                invalid_option()

def invalid_option():
     print("Você digitou uma opção inválida")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]