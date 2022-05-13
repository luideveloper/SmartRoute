# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

from driver import *
from vehicles import *
from routes import *
from business import *

def start_bd():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), user VARCHAR(200), password VARCHAR(200), office VARCHAR(100), security_key VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (codigo integer, marca VARCHAR(200), modelo VARCHAR(200), data_fabricação VARCHAR(200), km_atual VARCHAR(200), ultima_km_manutencao VARCHAR(200));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    con.commit()
    con.close()
    menu()

def menu():
    print("\x1b[2J\x1b[1;1H")
    print("=== BEM VINDO AO SMART ROUTE ===")
    print("\n[ 1 ] Faça login")
    print("[ 2 ] Criar conta")
    print("[ 3 ] Recuperar conta")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        login()
    elif (option == 2):
        create_account()
    elif (option == 3):
        recovery_account()
    else:
        invalid_option()

def menu_business():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Olá, seja bem vindo ao painel | Setor: Administrativo ===\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa")
    print("[ 5 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA MOTORISTA ===")
        print("\n[ 1 ] Cadastrar motorista")
        print("[ 2 ] Visualizar motoristas cadastrados")
        print("[ 3 ] Editar motorista")
        print("[ 4 ] Remover motorista")
        print("[ 5 ] Voltar ao menu principal\n")

        driver = int(input("Digite o número da opção que deseja: "))

        if (driver == 1):
            print("\x1b[2J\x1b[1;1H")
            register_driver()
            print("")
            
        elif (driver == 2):
            print("\x1b[2J\x1b[1;1H")
            read_driver()
            print("")
        
        elif (driver == 3):
            print("\x1b[2J\x1b[1;1H")
            update_driver()
            print("")
        
        elif (driver == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_driver()
            print("")
        
        elif (driver == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA VEÍCULOS ===")
        print("\n[ 1 ] Cadastrar veículos")
        print("[ 2 ] Visualizar veículos cadastrados")
        print("[ 3 ] Editar veículos")
        print("[ 4 ] Remover veículos")
        print("[ 5 ] Voltar ao menu principal\n")

        vehicles = int(input("Digite o número da opção que deseja: "))

        if (vehicles == 1):
            print("\x1b[2J\x1b[1;1H")
            register_vehicles()
            print("")
            
        elif (vehicles == 2):
            print("\x1b[2J\x1b[1;1H")
            read_vehicles()
            print("")
        
        elif (vehicles == 3):
            print("\x1b[2J\x1b[1;1H")
            update_vehicles()
            print("")
        
        elif (vehicles == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_vehicles()
            print("")
        
        elif (vehicles == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

    elif (option == 3):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA ROTAS ===")
        print("\n[ 1 ] Cadastrar rotas")
        print("[ 2 ] Visualizar rotas cadastrados")
        print("[ 3 ] Editar rotas")
        print("[ 4 ] Remover rotas")
        print("[ 5 ] Voltar ao menu principal\n")

        routes = int(input("Digite o número da opção que deseja: "))

        if (routes == 1):
            print("\x1b[2J\x1b[1;1H")
            register_routes()
            print("")
            
        elif (routes == 2):
            print("\x1b[2J\x1b[1;1H")
            read_routes()
            print("")
        
        elif (routes == 3):
            print("\x1b[2J\x1b[1;1H")
            update_routes()
            print("")
        
        elif (routes == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_routes()
            print("")
        
        elif (routes == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

    elif (option == 4):
        print("=== ÁREA EMPRESA ===")
        print("\n[ 1 ] Cadastrar conta")
        print("[ 2 ] Recuperar conta")
        print("[ 3 ] Visualizar relatório")
        print("[ 4 ] Excluir contas")
        print("[ 5 ] Voltar ao menu principal\n")

        business = int(input("Digite o número da opção que deseja: "))

        if (business == 1):
            print("\x1b[2J\x1b[1;1H")
            register_routes()
            print("")
            
        elif (business == 2):
            print("\x1b[2J\x1b[1;1H")
            read_routes()
            print("")
        
        elif (business == 3):
            print("\x1b[2J\x1b[1;1H")
            update_routes()
            print("")
        
        elif (business == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_routes()
            print("")
        
        elif (business == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

    elif (option == 5):
        print("\x1b[2J\x1b[1;1H")
        exit()

    else:
        invalid_option()

def menu_driver():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Olá, seja bem vindo ao painel | Setor: Motorista ===\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa\n")

    option = int(input("Digite o número da opção que deseja: "))

def menu_operational():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Olá, seja bem vindo ao painel | Setor: Operacional ===\n")
    print("[ 1 ] Visualizar motoristas")
    print("[ 2 ] Visualizar veículos")
    print("[ 3 ] Visualizar rotas")
    print("[ 4 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        read_driver()
    elif (option == 2):
        read_vehicles()
    elif (option == 3):
        read_routes()
    elif (option == 4):
        print("\x1b[2J\x1b[1;1H")
        exit()

def login():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT user, password, office FROM users;"
    cursor.execute(cod_query_read)

    lista_usuarios = []
    lista_senha = []
    
    for linha in cursor.fetchall():
        user_bd = linha[0]
        password_bd = linha[1]
        office_bd = linha[2]
        lista_usuarios.append(user_bd)
        lista_senha.append(password_bd)
    
    business = "Administrativo"
    driver = "Motorista"
    operational = "Operacional"

    print("\n=== LOGIN ===")
    user = input("\nDigite seu usuário: ")
    password = input("Digite sua senha: ")

    cod_query_read_2 = "SELECT user, office FROM users WHERE user=?;"
    cursor.execute(cod_query_read_2,(user,))
    for linha in cursor.fetchall():
        office_bd = linha[1]

    if (user in lista_usuarios and password in password_bd):
        if (business == office_bd):
            menu_business()
        elif (driver == office_bd):
            menu_driver()
        elif (operational == office_bd):
            menu_operational()
        else:
            print("Usuário com cargo não cadastrado")
    else:
        post_login_error()

def post_login_error():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Usuário ou senha errado ===")
    time.sleep(1)
    print("\nEscolha uma das opções\n")
    print("[ 1 ] Tentar novamente")
    print("[ 2 ] Recuperar senha")
    print("[ 3 ] Voltar ao menu principal")
    print("[ 4 ] Sair do sistema")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        login()
    elif (option == 2):
        recovery_account()
    elif (option == 3):
        menu()
    elif (option == 4):
        exit()
    else:
        invalid_option()

def create_account():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    key_company = "smartrouteclienttest"

    print("\n=== DIGITE A CHAVE DE PERMISSÃO===\n")
    print("Para poder criar uma conta e ter acesso no sistema, você precisa forncer a chave de permissão fornecida pela empresa\n")

    key = input("Chave de permissão: ")

    if (key == key_company):
        print("\x1b[2J\x1b[1;1H")
        print("\n=== CADASTRE-SE ===\n")
        name = input("Nome: ")
        cpf = input("CPF: ")
        user = input("Usuário: ")
        password = input("Senha: ")
        security_key = input("Chave de segurança: ")
        print("\n---------------------")
        
        print("\n[ 1 ] Administrativo")
        print("[ 2 ] Motorista")
        print("[ 3 ] Operacional")

        option = int(input("\nQual seu cargo? "))

        if (option == 1):
            office = "Administrativo"
        elif (option == 2):
            office = "Motorista"
        elif (option == 3):
            office = "Operacional"
        else:
            invalid_option()
        
        cod_query_creat = "INSERT INTO users (name,cpf,user,password,office,security_key) VALUES (?,?,?,?,?,?);"
        cursor.execute(cod_query_creat,(name,cpf,user,password,office,security_key))
        con.commit()
        print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
        con.close()
        time.sleep(3)
        menu()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Chave inválida")
        print("_____________________\n")
        print("Escolha uma das opções:\n")
        print("[ 1 ] Digitar novamente a chave")
        print("[ 2 ] Voltar ao menu anterior")
        print("[ 3 ] Sair do programa\n")

        option = int(input("O que você deseja? "))

        if (option == 1):
            create_account()
        elif (option == 2):
            menu()
        elif (option == 3):
            print("\x1b[2J\x1b[1;1H")
            exit()
        else:
            invalid_option()
            time.sleep(3)
            menu()

def recovery_account():
    print("\x1b[2J\x1b[1;1H")
    security_key = input("\nQual a chave de segurança da conta que deseja recuperar? ")
    print("\n== DIGITE UMA NOVA SENHA ==\n")
    new_password = input("Senha nova: ")
    repeat_new_password = input("Repita a senha nova: ")
    if (new_password == repeat_new_password):
        con = sqlite3.connect("dados.db")
        cursor = con.cursor()
        cod_query_update = "UPDATE users SET password=? WHERE security_key=?"
        cursor.execute(cod_query_update,(new_password,security_key))
        con.commit()
        print("\n>> SENHA ATUALIZADA COM SUCESSO <<")
        time.sleep(3)
        con.close()
        menu()
    else:
        post_error_recovery_account()

def post_error_recovery_account():
    print("\n> As senhas digitadas não são iguais")
    time.sleep(2)
    print("\Deseja digitar novamente?\n")
    print("[ 1 ] sim")
    print("[ 2 ] não")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        recovery_account()
    elif (option == 2):
        menu()

def invalid_option():
    print("\x1b[2J\x1b[1;1H")
    print("Opção inválida")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]