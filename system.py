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
    cursor.execute("CREATE TABLE IF NOT EXISTS users (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), user VARCHAR(200), password VARCHAR(200), office VARCHAR(100), type_license VARCHAR(100), validity_license VARCHAR(100), security_key VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (reg integer, plate VARCHAR(200), vehicles_type VARCHAR(200), model VARCHAR(200), date VARCHAR(200), km_inital VARCHAR(200), km_now VARCHAR(200), PRIMARY KEY (reg));")
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
    print("[ 4 ] Sair do programa")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        login()
    elif (option == 2):
        create_account()
    elif (option == 3):
        recovery_account()
    elif (option == 4):
        print("\x1b[2J\x1b[1;1H")
        exit()
    else:
        invalid_option()

def menu_business():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Olá, seja bem vindo ao painel | Setor: Administrativo ===\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa")
    print("[ 5 ] Voltar ao menu anterior")
    print("[ 6 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA MOTORISTA ===")
        print("\n[ 1 ] Cadastrar motorista")
        print("[ 2 ] Visualizar motoristas")
        print("[ 3 ] Editar motorista")
        print("[ 4 ] Remover motorista")
        print("[ 5 ] Voltar ao menu anterior")
        print("[ 6 ] Sair do programa\n")

        driver = int(input("Digite o número da opção que deseja: "))

        if (driver == 1):
            print("\x1b[2J\x1b[1;1H")
            register_driver()
            post_action_business()
            
        elif (driver == 2):
            print("\x1b[2J\x1b[1;1H")
            read_driver()
            post_action_business()
        
        elif (driver == 3):
            print("\x1b[2J\x1b[1;1H")
            update_driver()
            post_action_business()
        
        elif (driver == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_driver()
            post_action_business()
        
        elif (driver == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()
        
        elif (driver == 6):
            print("\x1b[2J\x1b[1;1H")
            exit()

        else:
            invalid_option()

    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA VEÍCULOS ===")
        print("\n[ 1 ] Cadastrar veículos")
        print("[ 2 ] Visualizar veículos")
        print("[ 3 ] Editar veículos")
        print("[ 4 ] Remover veículos")
        print("[ 5 ] Voltar ao menu anterior")
        print("[ 6 ] Sair do programa\n")

        vehicles = int(input("Digite o número da opção que deseja: "))

        if (vehicles == 1):
            print("\x1b[2J\x1b[1;1H")
            register_vehicles()
            
        elif (vehicles == 2):
            print("\x1b[2J\x1b[1;1H")
            read_vehicles()
        
        elif (vehicles == 3):
            print("\x1b[2J\x1b[1;1H")
            update_vehicles()
        
        elif (vehicles == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_vehicles()
        
        elif (vehicles == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

        elif (vehicles == 6):
            print("\x1b[2J\x1b[1;1H")
            exit()

        else:
            invalid_option()

    elif (option == 3):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA ROTAS ===")
        print("\n[ 1 ] Cadastrar rotas")
        print("[ 2 ] Visualizar rotas")
        print("[ 3 ] Editar rotas")
        print("[ 4 ] Remover rotas")
        print("[ 5 ] Voltar ao menu anterior")
        print("[ 6 ] Sair do programa\n")

        routes = int(input("Digite o número da opção que deseja: "))

        if (routes == 1):
            print("\x1b[2J\x1b[1;1H")
            register_routes()          
            
        elif (routes == 2):
            print("\x1b[2J\x1b[1;1H")
            read_routes()
        
        elif (routes == 3):
            print("\x1b[2J\x1b[1;1H")
            update_routes()
        
        elif (routes == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_routes()
        
        elif (routes == 5):
            print("\x1b[2J\x1b[1;1H")
            menu_business()

        elif (routes == 6):
            print("\x1b[2J\x1b[1;1H")
            exit()

        else:
            invalid_option()

    elif (option == 4):
        print("\x1b[2J\x1b[1;1H")
        print("=== ÁREA EMPRESA ===")
        print("\n[ 1 ] Cadastrar conta")
        print("[ 2 ] Recuperar conta")
        print("[ 3 ] Atualizar cadastro")
        print("[ 4 ] Visualizar relatório")
        print("[ 5 ] Excluir contas")
        print("[ 6 ] Visualizar funcionários")
        print("[ 7 ] Voltar ao menu anterior")
        print("[ 8 ] Sair do programa\n")

        business = int(input("Digite o número da opção que deseja: "))

        if (business == 1):
            print("\x1b[2J\x1b[1;1H")
            creat_account()
            
        elif (business == 2):
            print("\x1b[2J\x1b[1;1H")
            recovery_account()
        
        elif (business == 3):
            print("\x1b[2J\x1b[1;1H")
            update_account()
        
        elif (business == 4):
            print("\x1b[2J\x1b[1;1H")
            print("Ainda em desenvolvimento")
        
        elif (business == 5):
            print("\x1b[2J\x1b[1;1H")
            remove_account()

        elif (business == 6):
            print("\x1b[2J\x1b[1;1H")
            read_employee()
            post_action_business()
        
        elif (business == 7):
            print("\x1b[2J\x1b[1;1H")
            menu_business()
        
        elif ():
            print("\x1b[2J\x1b[1;1H")
            exit()

        else:
            invalid_option()

    elif (option == 5):
        print("\x1b[2J\x1b[1;1H")
        menu()
    
    elif (option == 6):
        print("\x1b[2J\x1b[1;1H")
        exit()

    else:
        invalid_option()

def menu_driver():
    print("\x1b[2J\x1b[1;1H")
    print("\n=== Olá, seja bem vindo ao painel | Setor: Motorista ===\n")
    print("[ 1 ] Visualizar rotas")
    print("[ 2 ] Visualizar veículos")
    print("[ 3 ] Atualizar veículos")
    print("[ 4 ] Acessar área da empresa")
    print("[ 5 ] Voltar ao menu anterior")
    print("[ 6 ] Sair do programa\n")

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
    cod_query_read = "SELECT user FROM users;"
    cursor.execute(cod_query_read)

    list_users = []
    
    for linha in cursor.fetchall():
        user_bd = linha[0]
        list_users.append(user_bd)
    
    business = "Administrativo"
    driver = "Motorista"
    operational = "Operacional"

    print("\n=== LOGIN ===")
    user = input("\nDigite seu usuário: ")
    password = input("Digite sua senha: ")

    cod_query_read_2 = "SELECT user, password, office FROM users WHERE user=?;"
    cursor.execute(cod_query_read_2,(user,))
    for linha in cursor.fetchall():
        password_bd = linha[1]
        office_bd = linha[2]

    if (user in list_users and password == password_bd):
        if (business == office_bd):
            menu_business()
        elif (driver == office_bd):
            menu_driver()
        elif (operational == office_bd):
            menu_operational()
        else:
            print("Usuário com cargo não cadastrado")
        
    elif (user not in list_users):
        print("\x1b[2J\x1b[1;1H")
        print("=== Usuário incorreto ===")
        post_login_error()

    elif (password != password_bd):
        print("\x1b[2J\x1b[1;1H")
        print("=== Senha incorreta ===")
        post_login_error()

    else:
        error()

def post_login_error():
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

    key_company = "1"

    print("\n=== DIGITE A CHAVE DE PERMISSÃO===\n")
    print("Para poder criar uma conta e ter acesso no sistema, você precisa fornecer a chave de permissão fornecida pela empresa\n")

    key = input("Chave de permissão: ")

    if (key == key_company):
        print("\x1b[2J\x1b[1;1H")
        print("\n=== CADASTRE-SE ===\n")

        print("Setores:")
        print("\n[ 1 ] Administrativo")
        print("[ 2 ] Motorista")
        print("[ 3 ] Operacional")

        option = int(input("\nQual o seu setor? "))

        if (option == 1):
            office = "Administrativo"
        elif (option == 2):
            register_driver()
            menu()
        elif (option == 3):
            office = "Operacional"
        else:
            invalid_option()

        print("\x1b[2J\x1b[1;1H")
        name = input("Nome: ")
        cpf = input("CPF: ")
        user = input("Usuário: ")
        password = input("Senha: ")
        security_key = input("Chave de segurança: ")
        print("\n---------------------")

        cod_query_read = "SELECT cpf, user, security_key FROM users"
        cursor.execute(cod_query_read)

        list_cpf = []
        list_users = []
        list_security_key = []
    
        for linha in cursor.fetchall():
            cpf_bd = linha[0]
            user_bd = linha[1]
            security_key_bd = linha[2]

            list_cpf.append(cpf_bd)
            list_users.append(user_bd)
            list_security_key.append(security_key_bd)

        if (cpf in list_cpf):
            print("\x1b[2J\x1b[1;1H")
            print("=== ATENÇÃO ===\n")
            print("CPF existente em cadastro, cadastre outro CPF para finalizar o cadastro")
            time.sleep(6)
            create_account()

        elif (user in list_users):

            if (security_key in list_security_key):
                print("\x1b[2J\x1b[1;1H")
                print("=== ATENÇÃO ===\n")
                print("Usuário e chave de segurança já existentes em cadastro, escolha outro usuário e outra chave para finalizar o cadastro")
                time.sleep(6)
                create_account()
            
            else:
                print("\x1b[2J\x1b[1;1H")
                print("=== ATENÇÃO ===\n")
                print("Usuário já existente em cadastro, escolha outro usuário para finalizar o cadastro")
                time.sleep(6)
                create_account()

        elif (security_key in list_security_key):
            print("\x1b[2J\x1b[1;1H")
            print("=== ATENÇÃO ===\n")
            print("Chave de segurança já existente em cadastro, escolha outra chave para finalizar o cadastro")
            time.sleep(6)
            create_account()
        else:
            cod_query_creat = "INSERT INTO users (name,cpf,user,password,office,security_key) VALUES (?,?,?,?,?,?);"
            cursor.execute(cod_query_creat,(name,cpf,user,password,office,security_key))
            con.commit()
            print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
            con.close()
            time.sleep(4)
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
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    security_key = input("\nQual a chave de segurança da conta que deseja recuperar? ")

    cod_query_read = "SELECT security_key FROM users WHERE security_key=?;"
    cursor.execute(cod_query_read,(security_key,))

    list_security_key = []
    
    for linha in cursor.fetchall():
        security_key_bd = linha[0]
        list_security_key.append(security_key_bd)

    if (security_key in list_security_key):
        print("\n== DIGITE UMA NOVA SENHA ==\n")
        new_password = input("Senha nova: ")
        repeat_new_password = input("Repita a senha nova: ")
        if (new_password == repeat_new_password):
            cod_query_update = "UPDATE users SET password=? WHERE security_key=?"
            cursor.execute(cod_query_update,(new_password,security_key))
            con.commit()
            print("\n>> SENHA ATUALIZADA COM SUCESSO <<")
            time.sleep(3)
            con.close()
            menu()
        else:
            post_error_recovery_account()
        
    else:
        print("\x1b[2J\x1b[1;1H")
        print("=== ATENÇÃO ===\n")
        print("Chave de seguranção não encontrada, por favor informe a chave correta")
        time.sleep(4)
        recovery_account()

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

def post_action_business():
    print("\x1b[2J\x1b[1;1H")
    print("Opções\n")
    print("[ 1 ] Voltar ao painel de funções")
    print("[ 2 ] Sair do programa")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        menu_business()
    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        exit()

def post_action_driver():
    print("\x1b[2J\x1b[1;1H")
    print("Opções\n")
    print("[ 1 ] Voltar ao painel de funções")
    print("[ 2 ] Sair do programa")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        menu_driver()
    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        exit()

def post_action_operational():  	
    print("\x1b[2J\x1b[1;1H")
    print("Opções\n")
    print("[ 1 ] Voltar ao painel de funções")
    print("[ 2 ] Sair do programa")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        menu_operational()
    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        exit()

def invalid_option():
    print("\x1b[2J\x1b[1;1H")
    print("Opção inválida")

def error():
    print("=== Ocorreu um erro no programa ===")
    time.sleep(3)
    menu()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]