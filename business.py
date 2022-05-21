# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

from system import *
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
        cpf = input("\nQual o cpf da conta que deseja atualizar? ")
        cpf = cpf.replace(" ", "").lower()

        cod_query_read = "SELECT cpf, security_key FROM users WHERE cpf=?;"
        cursor.execute(cod_query_read,(cpf,))

        list_cpf = []
        
        for linha in cursor.fetchall():
            cpf_bd = linha[0]
            security_key_bd = linha[1]
            list_cpf.append(cpf_bd)

        if (cpf in list_cpf):
            print("\x1b[2J\x1b[1;1H")
            security_key = input("\nQual a chave de segurança da conta que deseja recuperar? ")
            if (security_key == security_key_bd):
                print("\x1b[2J\x1b[1;1H")
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
                print("=== ATENÇÃO ==\n")
                print(">> Chave de segurança errada")
                time.sleep(3)
                print("\x1b[2J\x1b[1;1H")
                print("Escolha uma das opções:\n")
                print("[ 1 ] Tentar novamente")
                print("[ 2 ] Voltar ao menu principal")

                option = int(input("\nO que você deseja? "))

                if (option == 1):
                    recovery_account()
                elif (option == 2):
                    menu()
                else:
                    invalid_option()
    elif (option == 2):
        update_driver()
    elif (option == 3):
        print("\x1b[2J\x1b[1;1H")
        cpf = input("\nQual o cpf do funcionário que deseja atualizar os dados? ")
        cpf = cpf.replace(" ", "").lower()

        cod_query_read = "SELECT cpf, security_key FROM users WHERE cpf=?;"
        cursor.execute(cod_query_read,(cpf,))

        list_cpf = []
        
        for linha in cursor.fetchall():
            cpf_bd = linha[0]
            security_key_bd = linha[1]
            list_cpf.append(cpf_bd)

        if (cpf in list_cpf):
            print("\x1b[2J\x1b[1;1H")
            security_key = input("\nQual a chave de segurança da conta que deseja recuperar? ")
            if (security_key == security_key_bd):
                print("\x1b[2J\x1b[1;1H")
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
                print("=== ATENÇÃO ==\n")
                print(">> Chave de segurança errada")
                time.sleep(3)
                print("\x1b[2J\x1b[1;1H")
                print("Escolha uma das opções:\n")
                print("[ 1 ] Tentar novamente")
                print("[ 2 ] Voltar ao menu principal")

                option = int(input("\nO que você deseja? "))

                if (option == 1):
                    recovery_account()
                elif (option == 2):
                    menu()
                else:
                    invalid_option()
    else:
        invalid_option()

    

    

def remove_account():
    print("Ainda em desenvolvimento")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]