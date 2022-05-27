# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

from driver import *

def read_employee():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT name, cpf, user, office FROM users;"
    cursor.execute(cod_query_read)
    print("\x1b[2J\x1b[1;1H")
    print("== FUNCIONÁRIOS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("\nNome:", linha[0])
        print("CPF:", linha[1])
        print("Usuário:", linha[2])
        print("Setor:", linha[3])
        print("\n-------------------")
    time.sleep(15)
    con.close()

def update_account():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cpf = input("\nQual o cpf do funcionário que deseja atualizar os dados? ")
    cpf = cpf.replace(" ", "").lower()

    cod_query_read = "SELECT user, cpf, office FROM users"
    cursor.execute(cod_query_read)

    list_users = []
    list_cpf = []
        
    for linha in cursor.fetchall():
        user_bd = linha[0]
        cpf_bd = linha[1]
        office_bd = linha[2]
        list_users.append(user_bd)
        list_cpf.append(cpf_bd)
    
    administrativo = "Administrativo"
    motorista = "Motorista"
    operacional = "Operacional"

    if (cpf in list_cpf):

        if (office_bd == administrativo):
            print("\n== DIGITE OS NOVOS DADOS ==\n")
            new_name = input("Nome: ")
            new_user = input("Usuário: ")
            new_user = new_user.replace(" ", "").lower()
            new_password = input("Senha nova: ")
            repeat_new_password = input("Repita a senha nova: ")
            new_security_key = input("Chave de segurança: ")

            if (new_password == repeat_new_password):
                if (new_user in list_users):
                    print("\x1b[2J\x1b[1;1H")
                    print("=== ATENÇÃO ===\n")
                    print(">> Usuário indisponível, escolha outro usuário para efetuar a atualização do cadastro")
                    time.sleep(5)
                    con.close()
                else:
                    cod_query_update = "UPDATE users SET name=?, user=?, password=?, security_key=? WHERE cpf=?"
                    cursor.execute(cod_query_update,(new_name,new_user,new_password,new_security_key,cpf))
                    con.commit()
                    print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                    time.sleep(3)
                    con.close()
            else:
                post_error_recovery_account()

        elif (office_bd == motorista):
            update_driver()

        elif (office_bd == operacional):
            print("\n== DIGITE OS NOVOS DADOS ==\n")
            new_name = input("Nome: ")
            new_user = input("Usuário: ")
            new_user = new_user.replace(" ", "").lower()
            new_password = input("Senha nova: ")
            repeat_new_password = input("Repita a senha nova: ")
            new_security_key = input("Chave de segurança: ")

            if (new_password == repeat_new_password):
                if (new_user in list_users):
                    print("\x1b[2J\x1b[1;1H")
                    print("=== ATENÇÃO ===\n")
                    print(">> Usuário indisponível, escolha outro usuário para efetuar a atualização do cadastro")
                    time.sleep(5)
                    con.close()
                else:
                    cod_query_update = "UPDATE users SET name=?, user=?, password=?, security_key=? WHERE cpf=?"
                    cursor.execute(cod_query_update,(new_name,new_user,new_password,new_security_key,cpf))
                    con.commit()
                    print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                    time.sleep(3)
                    con.close()
            else:
                post_error_recovery_account()

        else:
            print("\x1b[2J\x1b[1;1H")
            print("=== ATENÇÃO ===\n")
            print(">> Funcionário com cargo não identificado")
            time.sleep(5)
            con.close()
    else:
        print("=== ATENÇÃO ===\n")
        print(">> Funcionário não encontrado")
        time.sleep(5)
        con.close()

def remove_account():
    print("\x1b[2J\x1b[1;1H")
    print("\n== REMOVER CADASTRO ==\n")
    cpf = int(input("Qual o cpf do cliente a remover? "))
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cod_query_read = "SELECT name, cpf, user, office FROM users WHERE cpf=?;"
    cursor.execute(cod_query_read,(cpf,))
    print("\x1b[2J\x1b[1;1H")
    print("> CADASTRO")
    for linha in cursor.fetchall():
        print("\nNome:", linha[0])
        print("CPF:", linha[1])
        print("Usuário:", linha[2])
        print("Setor:", linha[3])
        print("\n-------------------")
    
    cod_query_remove = "DELETE FROM users WHERE cpf ="
    cursor.execute(cod_query_remove+str(cpf))
    con.commit()
    print("\n>> CADASTRO REMOVIDO DO SISTEMA <<")
    time.sleep(3)
    con.close()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]