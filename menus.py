import sqlite3
import time

from login import *
from system import *
from create_bd import *
from accounts import *
from driver import *
from vehicles import *
from routes import *

def first_menu():
    print("\nOlá, seja bem vindo ao Smart Route, o que você deseja?\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa\n")

def back_menu():
    print("\nOperação finalizada, o que você deseja?\n")
    print("[ 1 ] Retornar ao menu")
    print("[ 2 ] Encerrar o programa")

    option = input("O que você deseja? ")

    if (option == 1):
        full_menu()
    elif (option == 2):
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
        print("\x1b[2J\x1b[1;1H")
        if (option == 1):
            print("=== ÁREA MOTORISTA ===")
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
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (driver == 4):
                remove_driver()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (driver == 5):
                first_menu()
                print("")

            else:
                invalid_option()
        
        print("\x1b[2J\x1b[1;1H")
        if (option == 2):
            print("=== ÁREA VEÍCULOS ===")
            print("\n[ 1 ] Cadastrar veículos")
            print("[ 2 ] Visualizar veículos cadastrados")
            print("[ 3 ] Editar veículos")
            print("[ 4 ] Remover veículos")
            print("[ 5 ] Voltar ao menu principal\n")

            vehicles = int(input("Digite o número da opção que deseja: "))

            if (vehicles == 1):
                register_vehicles()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (vehicles == 2):
                read_vehicles()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (vehicles == 3):
                update_vehicles()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (vehicles == 4):
                remove_vehicles()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (vehicles == 5):
                first_menu()
                print("")

            else:
                invalid_option()

        print("\x1b[2J\x1b[1;1H")
        if (option == 3):
            print("=== ÁREA ROTAS ===")
            print("\n[ 1 ] Cadastrar rotas")
            print("[ 2 ] Visualizar rotas cadastrados")
            print("[ 3 ] Editar rotas")
            print("[ 4 ] Remover rotas")
            print("[ 5 ] Voltar ao menu principal\n")

            routes = int(input("Digite o número da opção que deseja: "))

            if (routes == 1):
                register_routes()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (routes == 2):
                read_routes()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (routes == 3):
                update_routes()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (routes == 4):
                remove_routes()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (routes == 5):
                first_menu()
                print("")

            else:
                invalid_option()

        print("\x1b[2J\x1b[1;1H")
        if (option == 4):
            print("=== ÁREA EMPRESA ===")
            print("\n[ 1 ] Cadastrar conta")
            print("[ 2 ] Recuperar conta")
            print("[ 3 ] Visualizar relatório")
            print("[ 4 ] Excluir contas")
            print("[ 5 ] Voltar ao menu principal\n")

            accounts = int(input("Digite o número da opção que deseja: "))

            if (accounts == 1):
                creat_account()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (accounts == 2):
                recovery_account()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (accounts == 3):
                report_account()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (accounts == 4):
                remove_account()
                print("\x1b[2J\x1b[1;1H")
                back_menu()
                print("")

            elif (accounts == 5):
                first_menu()
                print("")
            
            elif (accounts == 6):
                read_account()
                print("")

            else:
                invalid_option()
