# Importação de bibliotecas ↓

import sqlite3
import time

# Cadastro de motorista no sistema | Registro ↓

def register_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("SmartRoute\database\dados.db")
    cursor = con.cursor()
    office = "Motorista" # Definição do cargo (fixo) para inserção no banco de dados
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

    # Verificação de dados no cadastro

    # Verifica se o cpf repassado já está cadastrado ↓

    if (cpf in list_cpf):
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print("CPF existente em cadastro, cadastre outro CPF para finalizar o cadastro")
        time.sleep(6)
        con.close()

    # Verifica se a quantidade de caracteres do cpf repassado está correta ↓
        
    elif (len(cpf) > 11 or len(cpf) < 11):
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print(">> Quantidade de caracteres do CPF inválida")
        time.sleep(6)
        con.close()
    
    # Verifica se o user repassado já está cadastrado ↓

    elif (user in list_users):
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print("Usuário já existente em cadastro, escolha outro usuário para finalizar o cadastro")
        time.sleep(6)
        con.close()

    # Se passar em todas as verificações, o cadastro é realizado ↓

    else:
        cod_query_creat = "INSERT INTO users (name,cpf,user,password,office,type_license,validity_license,security_key) VALUES (?,?,?,?,?,?,?,?);"
        cursor.execute(cod_query_creat,(name,cpf,user,password,office,type_license,validity_license,security_key))
        con.commit()
        print("\n>> CADASTRADO REALIZADO COM SUCESSO <<")
        time.sleep(3)
        con.close()

# Ler todos os motoristas cadastrados no sistema ↓

def read_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("SmartRoute\database\dados.db")
    cursor = con.cursor()
    office = "Motorista"
    cod_query_read = "SELECT name, cpf, type_license, validity_license FROM users WHERE office =?;"
    cursor.execute(cod_query_read,(office,))
    print("\n== MOTORISTAS CADASTRADOS ==")

    # Percorre as informações do BD e imprime ↓

    for linha in cursor.fetchall():
        print("\nNome:", linha[0])
        print("CPF:", linha[1])
        print("Categoria da Habilitação:", linha[2])
        print("Validade da Habilitação:", linha[3])
        print("\n-------------------")
    time.sleep(10)
    con.close()

# Atualização de cadastro ↓

def update_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("SmartRoute\database\dados.db")
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
    
    cod_query_read2 = "SELECT user, cpf FROM users WHERE cpf=?;"
    cursor.execute(cod_query_read2,(cpf,))
    
    for linha in cursor.fetchall():
        user_bd2 = linha[0]

    # Se o cpf que foi repassado estiver cadastrado o usuário segue na funcionalidade ↓
    
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
                cod_query_update = "UPDATE users SET name=?, user=?, password=?, type_license=?, validity_license=?, security_key=? WHERE cpf=?"
                cursor.execute(cod_query_update,(new_name,new_user,new_password,new_type_license,new_validity_license,new_security_key,cpf))
                con.commit()
                print("\n>> CADASTRO ATUALIZADO COM SUCESSO <<")
                time.sleep(3)
                con.close()
        else:
            print("\x1b[2J\x1b[1;1H")
            print("\n== As senhas digitadas não são iguais ==\n")
            time.sleep(3)
            con.commit()
            con.close()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print(">> Funcionário não encontrado")
        time.sleep(5)
        con.close()