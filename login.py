import sqlite3
import time

from menus import *

def menu_login():
    print("\n=== BEM VINDO AO SMART ROUTE ===")
    print("\n[ 1 ] Faça login")
    print("[ 2 ] Criar conta")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        login()
    elif (option == 2):
        create_account()
    else:
        invalid_option()

def create_account():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    
    print("\x1b[2J\x1b[1;1H")
    print("\n=== CADASTRE-SE ===\n")
    name = input("Nome: ")
    cpf = input("CPF: ")
    user = input("Usuário: ")
    password = input("Senha: ")
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
    
    cod_query_creat = "INSERT INTO users (name,cpf,user,password,office) VALUES (?,?,?,?,?);"
    cursor.execute(cod_query_creat,(name,cpf,user,password,office))
    con.commit()
    print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
    time.sleep(3)
    con.close()


def login():
    con = sqlite3.connect("SmartRoute/dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT user, password FROM users;"
    cursor.execute(cod_query_read)

    lista_usuarios = []
    lista_senha = []
    for linha in cursor.fetchall():
        user_bd = linha[0]
        password_bd = linha[1]
        lista_usuarios.append(user_bd)
        lista_senha.append(password_bd)

    user = input("\nDigite seu usuário: ")
    password = input("Digite sua senha: ")
    if (user in lista_usuarios and password in password_bd):
        full_menu()
        print("")
    else:
        post_check_menu()


'''def check():
    con = sqlite3.connect("SmartRoute/dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT user, password FROM accounts;"
    cursor.execute(cod_query_read)

    for linha in cursor.fetchall():
        user_bd = linha[0]
        password_bd = linha[1]
        user = input("\nDigite seu usuário: ")
        password = input("Digite sua senha: ")
        if (user == user_bd and password == password_bd):
            register_driver()
            print("")
        else:
            post_check_menu()'''
            
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