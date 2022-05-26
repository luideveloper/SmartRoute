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

    print("Qual o setor da conta que deseja atualiza?")
    print("\n[ 1 ] Administrativo")
    print("[ 2 ] Motorista")
    print("[ 3 ] Operacional")

    option = int(input("\nQual o seu setor? "))

    if (option == 1):
        print("\x1b[2J\x1b[1;1H")
        cpf = input("\nQual o cpf da conta que deseja atualizar? ")
        cpf = cpf.replace(" ", "").lower()

        cod_query_read = "SELECT cpf FROM users WHERE cpf=?;"
        cursor.execute(cod_query_read,(cpf,))

        list_cpf = []
        
        for linha in cursor.fetchall():
            cpf_bd = linha[0]
            security_key_bd = linha[1]
            list_cpf.append(cpf_bd)

        if (cpf in list_cpf):
            print("\n== DIGITE OS NOVOS DADOS ==\n")
            new_name = input("Nome: ")
            new_cpf = input("CPF: ")
            new_cpf = new_cpf.replace(" ", "").lower()
            new_user = input("Usuário: ")
            new_user = new_user.replace(" ", "").lower()
            new_password = input("Senha nova: ")
            repeat_new_password = input("Repita a senha nova: ")
            new_security_key = input("Chave de segurança: ")

            if (new_password == repeat_new_password):
                cod_query_update = "UPDATE users SET name=?, cpf=?, user=?, password=?, security_key=? WHERE security_key=?"
                cursor.execute(cod_query_update,(new_name,new_cpf,new_user,new_password,new_security_key,cpf))
                con.commit()
                print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                time.sleep(3)
                con.close()
            else:
                post_error_recovery_account()
        else:
            print("=== ATENÇÃO ===\n")
            print(">> Funcionário não encontrado")
            time.sleep(5)
            con.close()

    elif (option == 2):
        update_driver()

    elif (option == 3):
        cpf = input("\nQual o cpf da conta que deseja atualizar? ")
        cpf = cpf.replace(" ", "").lower()

        cod_query_read = "SELECT cpf FROM users WHERE cpf=?;"
        cursor.execute(cod_query_read,(cpf,))

        list_cpf = []
        
        for linha in cursor.fetchall():
            cpf_bd = linha[0]
            security_key_bd = linha[1]
            list_cpf.append(cpf_bd)

        if (cpf in list_cpf):
            print("\n== DIGITE OS NOVOS DADOS ==\n")
            new_name = input("Nome: ")
            new_cpf = input("CPF: ")
            new_cpf = new_cpf.replace(" ", "").lower()
            new_user = input("Usuário: ")
            new_user = new_user.replace(" ", "").lower()
            new_password = input("Senha nova: ")
            repeat_new_password = input("Repita a senha nova: ")
            new_security_key = input("Chave de segurança: ")

            if (new_password == repeat_new_password):
                cod_query_update = "UPDATE users SET name=?, cpf=?, user=?, password=?, security_key=? WHERE security_key=?"
                cursor.execute(cod_query_update,(new_name,new_cpf,new_user,new_password,new_security_key,cpf))
                con.commit()
                print("\n>> CADASTRO ATUALIZADA COM SUCESSO <<")
                time.sleep(3)
                con.close()
            else:
                post_error_recovery_account()
        else:
            print("=== ATENÇÃO ===\n")
            print(">> Funcionário não encontrado")
            time.sleep(5)
            con.close()

    else:
        invalid_option() 

def remove_account():
    print("Ainda em desenvolvimento")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]