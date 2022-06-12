# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

# Importação de bibliotecas ↓

import sqlite3
import time

# Importação de funções de arquivos externos ↓

from driver import *

# Ler todos os usuários cadastrados no sistema ↓

def read_employee():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT name, cpf, user, office FROM users;"
    cursor.execute(cod_query_read)
    print("\x1b[2J\x1b[1;1H")
    print("== FUNCIONÁRIOS CADASTRADOS ==\n")

    # Percorre as informações do BD e imprime ↓

    for linha in cursor.fetchall():
        print("\nNome:", linha[0])
        print("CPF:", linha[1])
        print("Usuário:", linha[2])
        print("Setor:", linha[3])
        print("\n-------------------")
    time.sleep(10)
    con.close()

# Atualização de cadastro ↓

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

    cod_query_read2 = "SELECT user, cpf FROM users WHERE cpf=?;"
    cursor.execute(cod_query_read2,(cpf,))
    
    for linha in cursor.fetchall():
        user_bd2 = linha[0]
    
    administrativo = "Administrativo"
    motorista = "Motorista"
    operacional = "Operacional"

    # Se o cpf que foi repassado estiver cadastrado o usuário segue na funcionalidade ↓

    if (cpf in list_cpf):

        # Identificação do setor do usuário ↓

        if (office_bd == administrativo):
            print("\n== DIGITE OS NOVOS DADOS ==\n")
            new_name = input("Nome: ")
            new_user = input("Usuário: ")
            new_user = new_user.replace(" ", "").lower()
            new_password = input("Senha nova: ")
            repeat_new_password = input("Repita a senha nova: ")
            new_security_key = input("Chave de segurança: ")

            # Verifica se nova senha foi digitada corretamente na repetição ↓
            
            if (new_password == repeat_new_password):
                
                # Se o user for repetido, a atualização será realizada ↓

                if (new_user == user_bd2):
                    cod_query_update = "UPDATE users SET name=?, user=?, password=?, security_key=? WHERE cpf=?"
                    cursor.execute(cod_query_update,(new_name,new_user,new_password,new_security_key,cpf))
                    con.commit()
                    print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                    time.sleep(3)
                    con.close()
                
                # Verifica se o novo usuário já está cadastrado ↓

                elif (new_user in list_users):
                    print("\x1b[2J\x1b[1;1H")
                    print("== ATENÇÃO ==\n")
                    print(">> Usuário indisponível, escolha outro usuário para efetuar a atualização do cadastro")
                    time.sleep(5)
                    con.close()

                # Caso o novo usuário não esteja em uso, a atualização será realizada ↓
    
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
                    print("== ATENÇÃO ==\n")
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
            print("== ATENÇÃO ==\n")
            print(">> Funcionário com cargo não identificado")
            time.sleep(5)
            con.close()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print(">> Funcionário não encontrado")
        time.sleep(5)
        con.close()

# Remoção de cadastro no sistema ↓

def remove_account():
    print("\x1b[2J\x1b[1;1H")
    print("\n== REMOVER CADASTRO ==\n")
    cpf = input("Qual o cpf do funcionário que deseja remover? ")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cod_query_read = "SELECT cpf FROM users"
    cursor.execute(cod_query_read)

    list_cpf = []
        
    for linha in cursor.fetchall():
        cpf_bd = linha[0]
        list_cpf.append(cpf_bd)

    # Se o cpf que foi repassado estiver cadastrado o usuário segue na funcionalidade ↓

    if (cpf in list_cpf):
        cod_query_remove = "DELETE FROM users WHERE cpf=?"
        cursor.execute(cod_query_remove,(cpf,))
        con.commit()
        print("\n>> CADASTRO REMOVIDO DO SISTEMA <<")
        time.sleep(3)
        con.close()
        
    else:
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print(">> Cadastro não encontrado")
        time.sleep(3)
        con.close()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]