# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

def register_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    office = "Motorista"
    name = input("Nome: ")
    cpf = input("CPF: ")
    user = input("Usuário: ")
    password = input("Senha: ")
    type_license = input("Categoria da Habilitação: ")
    validity_license = input("Validade da Habilitação: ")
    security_key = input("Chave de segurança: ")

    cod_query_read = "SELECT cpf, user FROM users"
    cursor.execute(cod_query_read)

    list_cpf = []
    list_users = []
        
    for linha in cursor.fetchall():
        cpf_bd = linha[0]
        user_bd = linha[1]

        list_cpf.append(cpf_bd)
        list_users.append(user_bd)

    # Start - Registration Validations

    if (cpf in list_cpf):
        print("\x1b[2J\x1b[1;1H")
        print("=== ATENÇÃO ===\n")
        print("CPF existente em cadastro, cadastre outro CPF para finalizar o cadastro")
        time.sleep(6)
        con.close()
        
    elif (len(cpf) > 11 or len(cpf) < 11):
        print("\x1b[2J\x1b[1;1H")
        print("=== ATENÇÃO ===\n")
        print(">> Quantidade de caracteres do CPF inválida")
        time.sleep(6)
        con.close()

    elif (user in list_users):
        print("\x1b[2J\x1b[1;1H")
        print("=== ATENÇÃO ===\n")
        print("Usuário já existente em cadastro, escolha outro usuário para finalizar o cadastro")
        time.sleep(6)
        con.close()

    # End - Registration Validations

    else:
        cod_query_creat = "INSERT INTO users (name,cpf,user,password,office,type_license,validity_license,security_key) VALUES (?,?,?,?,?,?,?,?);"
        cursor.execute(cod_query_creat,(name,cpf,user,password,office,type_license,validity_license,security_key))
        con.commit()
        print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
        time.sleep(3)
        con.close()

def read_driver():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    office = "Motorista"
    cod_query_read = "SELECT name, cpf, type_license, validity_license FROM users WHERE office =?;"
    cursor.execute(cod_query_read,(office,))
    print("\n== MOTORISTAS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("\nNome:", linha[0])
        print("CPF:", linha[1])
        print("Categoria da Habilitação:", linha[2])
        print("Validade da Habilitação:", linha[3])
        print("\n-------------------")
    time.sleep(5)
    con.close()

def update_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cpf = input("\nQual o cpf do funcionário que deseja atualizar os dados? ")
    cpf = cpf.replace(" ", "").lower()
    
    cod_query_read = "SELECT user, cpf FROM users"
    cursor.execute(cod_query_read)

    list_users = []
    list_cpf = []
    
    for linha in cursor.fetchall():
        user_bd = linha[0]
        cpf_bd = linha[1]
        list_users.append(user_bd)
        list_cpf.append(cpf_bd)
    
    if (cpf in list_cpf):
        print("\x1b[2J\x1b[1;1H")
        print("\n== DIGITE OS NOVOS DADOS ==\n")
        new_name = input("Nome: ")
        new_user = input("Usuário: ")
        new_user = new_user.replace(" ", "").lower()
        new_type_license = input("Categoria da Habilitação: ")
        new_validity_license = input("Validade da Habilitação: ")
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
                cod_query_update = "UPDATE users SET name=?, user=?, password=?, type_license=?, validity_license=?, security_key=? WHERE cpf=?"
                cursor.execute(cod_query_update,(new_name,new_user,new_password,new_type_license,new_validity_license,new_security_key,cpf))
                con.commit()
                print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                time.sleep(3)
                con.close()
        else:
            post_error_recovery_account()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("=== ATENÇÃO ===\n")
        print(">> Funcionário não encontrado")
        time.sleep(5)
        con.close()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]