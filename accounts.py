# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

from menus import *
from create_bd import *
from driver import *
from vehicles import *
from routes import *

def creat_account():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    print("\n=== CADASTRE-SE NO SISTEMA ===\n")
    user = input("Usuário: ")
    password = input("Senha: ")
    security_key = input("Chave de segurança: ")
    cod_query_creat = "INSERT INTO accounts (user,password,security_key) VALUES (?,?,?);"
    cursor.execute(cod_query_creat,(user,password,security_key))
    con.commit()
    print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
    time.sleep(3)
    con.close()

def recovery_account():
    security_key = input("\nQual a chave de segurança da conta que deseja recuperar? ")
    print("\n== DIGITE UMA NOVA SENHA ==\n")
    new_password = input("Senha nova: ")
    repeat_new_password = input("Repita a senha nova: ")
    if (new_password == repeat_new_password):
        con = sqlite3.connect("dados.db")
        cursor = con.cursor()
        cod_query_update = "UPDATE accounts SET password=? WHERE security_key=?"
        cursor.execute(cod_query_update,(new_password,security_key))
        con.commit()
        print("\n>> SENHA ATUALIZADA COM SUCESSO <<")
        time.sleep(3)
        con.close()
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
        full_menu()

def read_account():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT user, password, security_key FROM accounts;"
    cursor.execute(cod_query_read)
    print("\n== CONTAS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("Usuário:", linha[0])
        print("Senha:", linha[1])
        print("Chave de segurança:", linha[2])
        print("\n-------------------")
    time.sleep(3)
    con.close()

def report_account():
    print("Ainda em desenvolvimento")

def remove_account():
    read_account()
    security_key = input("\nQual a chave de segurança do motorista que deseja remover? ")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_remove = "DELETE FROM accounts WHERE security_key ="
    cursor.execute(cod_query_remove+str(security_key))
    con.commit()
    print("\n>> CONTA EXCLUIDA COM SUCESSO <<")
    time.sleep(3)
    con.close()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]