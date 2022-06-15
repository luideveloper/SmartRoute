# Importação de bibliotecas ↓

import sqlite3
import time

# Importação de funções de arquivos externos ↓

from driver import *
from vehicles import *
from routes import *
from business import *

# Função responsável por iniciar a conexão com o banco de dados ↓

def start_bd():

    # Conexão + cursor ↓

    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    # Realiza a checagem e criação de tabelas no banco de dados ↓

    cursor.execute("CREATE TABLE IF NOT EXISTS users (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), user VARCHAR(200), password VARCHAR(200), office VARCHAR(100), type_license VARCHAR(100), validity_license VARCHAR(100), security_key VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (reg integer not null, plate VARCHAR(200), vehicles_type VARCHAR(200), model VARCHAR(200), date VARCHAR(200), km_initial VARCHAR(200), km_now VARCHAR(200), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (reg integer not null, route_code VARCHAR(200), route_start VARCHAR(200), route_end VARCHAR(200), stop VARCHAR(200), PRIMARY KEY(reg));")
    con.commit()
    con.close()
    menu()

# Menu principal ↓

def menu():
    print("\x1b[2J\x1b[1;1H")

    # Funcionalidades do menu principal do programa

    print("== BEM VINDO AO SMART ROUTE ==")
    print("\n[ 1 ] Faça login")
    print("[ 2 ] Criar conta")
    print("[ 3 ] Recuperar conta")
    print("[ 4 ] Sair do programa")

    try:
        option = int(input("\nO que você deseja? "))

        # Bloco de condicionais para realização das funcionalidades

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
            time.sleep(2)
            menu()
    
    # Tratamento de erros inesperados no programa

    except ValueError:
        value_error_input()

# Menu de funcionalidades do setor Administrativo ↓

def menu_business():
    print("\x1b[2J\x1b[1;1H")

    # Funcionalidades - Administrativo ↓

    print("\n== Olá, seja bem vindo ao painel | Setor: Administrativo ==\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas")
    print("[ 4 ] Acessar área da empresa")
    print("[ 5 ] Voltar ao menu anterior")
    print("[ 6 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        print("\x1b[2J\x1b[1;1H")
        print("== ÁREA MOTORISTA ==")
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
            remove_account()
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

        # Funcionalidades - Veículos

        print("== ÁREA VEÍCULOS ==")
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
            post_action_business()
            
        elif (vehicles == 2):
            print("\x1b[2J\x1b[1;1H")
            read_vehicles()
            post_action_business()
        
        elif (vehicles == 3):
            print("\x1b[2J\x1b[1;1H")
            update_vehicles()
            post_action_business()
        
        elif (vehicles == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_vehicles()
            post_action_business()
        
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

        # Funcionalidades - Rotas

        print("== ÁREA ROTAS ==")
        print("\n[ 1 ] Cadastrar rotas")
        print("[ 2 ] Visualizar rotas")
        print("[ 3 ] Editar rotas")
        print("[ 4 ] Remover rotas")
        print("[ 5 ] Voltar ao menu anterior")
        print("[ 6 ] Sair do programa\n")

        routes = int(input("Digite o número da opção que deseja: "))

        if (routes == 1):
            print("\x1b[2J\x1b[1;1H")
            create_routes()
            post_action_business()          
            
        elif (routes == 2):
            print("\x1b[2J\x1b[1;1H")
            read_routes()
            post_action_business()
        
        elif (routes == 3):
            print("\x1b[2J\x1b[1;1H")
            update_routes()
            post_action_business()
        
        elif (routes == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_routes()
            post_action_business()
        
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

        # Funcionalidades - Empresa

        print("== ÁREA EMPRESA ==")
        print("\n[ 1 ] Cadastrar conta")
        print("[ 2 ] Recuperar conta")
        print("[ 3 ] Atualizar cadastro")
        print("[ 4 ] Excluir contas")
        print("[ 5 ] Visualizar funcionários")
        print("[ 6 ] Voltar ao menu anterior")
        print("[ 7 ] Sair do programa\n")

        business = int(input("Digite o número da opção que deseja: "))

        if (business == 1):
            print("\x1b[2J\x1b[1;1H")
            create_account()
            
        elif (business == 2):
            print("\x1b[2J\x1b[1;1H")
            recovery_account()
        
        elif (business == 3):
            print("\x1b[2J\x1b[1;1H")
            update_account()
            time.sleep(4)
            post_action_business()
        
        elif (business == 4):
            print("\x1b[2J\x1b[1;1H")
            remove_account()
            post_action_business()
        
        elif (business == 5):
            print("\x1b[2J\x1b[1;1H")
            read_employee()
            post_action_business()

        elif (business == 6):
            print("\x1b[2J\x1b[1;1H")
            menu_business()
        
        elif (business == 7):
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

# Menu de funcionalidades do setor de Motoristas ↓

def menu_driver():
    print("\x1b[2J\x1b[1;1H")

    # Funcionalidades - Motorista ↓
    
    print("\n== Olá, seja bem vindo ao painel | Setor: Motorista ==\n")
    print("[ 1 ] Visualizar rotas")
    print("[ 2 ] Visualizar veículos")
    print("[ 3 ] Atualizar veículos")
    print("[ 4 ] Voltar ao menu anterior")
    print("[ 5 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        read_routes()
        post_action_driver()
    elif (option == 2):
        read_vehicles()
        post_action_driver()
    elif (option == 3):
        update_vehicles()
        post_action_driver()
    elif (option == 4):
        menu()
    elif (option == 5):
        print("\x1b[2J\x1b[1;1H")
        exit()
        
# Menu de funcionalidades do setor Operacional ↓

def menu_operational():
    print("\x1b[2J\x1b[1;1H")

    # Funcionalidades - Operacional ↓

    print("\n== Olá, seja bem vindo ao painel | Setor: Operacional ==\n")
    print("[ 1 ] Visualizar motoristas")
    print("[ 2 ] Visualizar veículos")
    print("[ 3 ] Visualizar rotas")
    print("[ 4 ] Voltar ao menu anterior")
    print("[ 5 ] Sair do programa\n")

    option = int(input("Digite o número da opção que deseja: "))

    if (option == 1):
        read_driver()
        post_action_operational()
    elif (option == 2):
        read_vehicles()
        post_action_operational()
    elif (option == 3):
        read_routes()
        post_action_operational()
    elif (option == 4):
        menu()
    elif (option == 5):
        print("\x1b[2J\x1b[1;1H")
        exit()

# Menu de login --> A parti do login o sistema identifica o setor do usuário e
# demostra um menu personalizado com as funcionalidades disponíveis para aquele setor ↓

def login():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    # Faz uma puxada de todos os usuários já cadastrados no banco 
    # e joga dentro de uma lista para realizar uma verificação se
    # o user passado pelo usuário realmente pertence a um cadastrto
    # já existente ↓

    cod_query_read = "SELECT user FROM users;"
    cursor.execute(cod_query_read)

    list_users = []
    
    for linha in cursor.fetchall():
        user_bd = linha[0]

        # Adicionando todos os usuários já existente na lista ↓

        list_users.append(user_bd)
    
    business = "Administrativo"
    driver = "Motorista"
    operational = "Operacional"

    print("\n== LOGIN ==")
    user = input("\nDigite seu usuário: ")
    user = user.replace(" ", "").lower()
    password = input("Digite sua senha: ")

    # Realizada a puxada dos dados do user que foi passado 
    # pelo usuário no login para identificação e verificações ↓

    cod_query_read_2 = "SELECT user, password, office FROM users WHERE user=?;"
    cursor.execute(cod_query_read_2,(user,))

    for linha in cursor.fetchall():
        password_bd = linha[1]
        office_bd = linha[2]

    # Verificação se o user repassado pertence a um cadastro existente
    # e se a senha repassada está correta (caso o cadastro exista) ↓

    if (user in list_users and password == password_bd):

        # Bloco de condicionais para a 
        # verificação do setor do usuário ↓

        if (business == office_bd):
            menu_business()
        elif (driver == office_bd):
            menu_driver()
        elif (operational == office_bd):
            menu_operational()
        else:
            print("Usuário com cargo não cadastrado")
    
    # Caso o usuário repassado no login não exista em
    # nenhum cadastro o programa informa ao o usuário ↓

    elif (user not in list_users):
        print("\x1b[2J\x1b[1;1H")
        print("== Usuário incorreto ==")
        post_login_error()
    
    # Caso o a senha repassada no login esteja 
    # errada o sistema informa ao usuário ↓

    elif (password != password_bd):
        print("\x1b[2J\x1b[1;1H")
        print("== Senha incorreta ==")
        post_login_error()

    # Erro inesperado no programa ↓

    else:
        error()

# Mensagem + menu pós erro login ↓

def post_login_error():
    print("\nEscolha uma das opções\n")
    print("[ 1 ] Tentar novamente")
    print("[ 2 ] Criar conta")
    print("[ 3 ] Recuperar senha")
    print("[ 4 ] Voltar ao menu principal")
    print("[ 5 ] Sair do sistema")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        login()
    elif (option == 2):
        create_account()
    elif (option == 3):
        recovery_account()
    elif (option == 4):
        menu()
    elif (option == 5):
        print("\x1b[2J\x1b[1;1H")
        exit()
    else:
        invalid_option()

# Criação de contas | Cadastro ↓

def create_account():
    print("\x1b[2J\x1b[1;1H")

    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    # Chave de permissão para criar uma conta no sistema ↓

    key_company = "keytest"

    print("\n== DIGITE A CHAVE DE PERMISSÃO ==\n")
    print("Para poder criar uma conta e ter acesso no sistema, você precisa fornecer a chave de permissão fornecida pela empresa\n")

    key = input("Chave de permissão: ")

    # Verificação da chave de permissão ↓

    if (key == key_company):
        print("\x1b[2J\x1b[1;1H")
        print("\n== CADASTRE-SE ==\n")

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
        cpf = cpf.replace(" ", "").lower()
        user = input("Usuário: ")
        user = user.replace(" ", "").lower()
        password = input("Senha: ")
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
            create_account()
        
        # Verifica se a quantidade de caracteres do cpf repassado está correta ↓

        elif (len(cpf) > 11 or len(cpf) < 11):
            print("\x1b[2J\x1b[1;1H")
            print("== ATENÇÃO ==\n")
            print(">> Quantidade de caracteres do CPF inválida")
            time.sleep(6)
            menu()

        # Verifica se o user repassado já está cadastrado ↓

        elif (user in list_users):
            print("\x1b[2J\x1b[1;1H")
            print("== ATENÇÃO ==\n")
            print("Usuário já existente em cadastro, escolha outro usuário para finalizar o cadastro")
            time.sleep(6)
            create_account()

        # Se passar em todas as verificações, o cadastro é realizado ↓

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

# Recuperação de contas --> senhas ↓

def recovery_account():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cpf = input("\nQual o cpf da conta que deseja recuperar? ")
    cpf = cpf.replace(" ", "").lower()

    # Puxa as informações de cadastro do cpf repassado ↓ 

    cod_query_read = "SELECT cpf, security_key FROM users WHERE cpf=?;"
    cursor.execute(cod_query_read,(cpf,))

    list_cpf = []
    
    for linha in cursor.fetchall():
        cpf_bd = linha[0]
        security_key_bd = linha[1]

        # Caso o cpf esteja cadastrado, ele será adicionado a essa lista
        # Se não estiver, a lista permanecera vazia

        list_cpf.append(cpf_bd)

    # Se o cpf que foi repassado estiver cadastrado e conter informações 
    # associadas, ele faz uma nova verificação: chave de segurança ↓

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
            print("== ATENÇÃO ==\n")
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

    # Caso o cpf repassado não contenha informações associadas e não esteja 
    # cadastrado programa informa ao usuário que o cpf não foi encontrado ↓
        
    else:
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print("Cadastro não encontrado, por favor informe o CPF correto")
        
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

# Mensagem + menu pós erro ao recuperação de conta ↓

def post_error_recovery_account():
    print("\x1b[2J\x1b[1;1H")
    print("\n== As senhas digitadas não são iguais ==\n")
    time.sleep(2)
    print("Deseja digitar novamente?\n")
    print("[ 1 ] sim")
    print("[ 2 ] não")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        recovery_account()
    elif (option == 2):
        menu()

# Menu de pós erro ao criar conta ↓

def post_action_create_account():
    print("\x1b[2J\x1b[1;1H")
    print("Opções\n")
    print("[ 1 ] Tentar novamente")
    print("[ 2 ] Voltar ao painel de funções")
    print("[ 3 ] Sair do programa")

    option = int(input("\nO que você deseja? "))

    if (option == 1):
        menu()
    elif (option == 2):
        menu()
    elif (option == 3):
        print("\x1b[2J\x1b[1;1H")
        exit()
    else:
        invalid_option()

# Toda vez que uma ação (funcionalidade) for realizada
# pelo setor em questão o usuário tem acesso ao
# menu ao menu de pós ação para poder realizar novas ações ↓

# Menu de pós ação | Administrativo ↓

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

# Menu de pós ação | Motorista ↓

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

# Menu de pós ação | Operacional ↓

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

# Quando o usuário digita um número que
# não é correspondente a nenhuma opção do menu
# o programa sinaliza que é o número digitado é
# uma opção inválida ↓

# Mensagem de opção inválida ↓

def invalid_option():
    print("\x1b[2J\x1b[1;1H")
    print("== ATENÇÃO ==\n")
    print(">> Opção inválida")

# Mensagem de erro no programa ↓

def error():
    print("\x1b[2J\x1b[1;1H")
    print("== ATENÇÃO ==\n")
    print(">> Ocorreu um erro no programa")
    time.sleep(4)
    menu()

# Mensagem de erro inesperado no programa ↓

def value_error_input():
    print("\x1b[2J\x1b[1;1H")
    print("== ATENÇÃO ==\n")
    print(">> Erro inesperado, o programa será reinicializado")
    time.sleep(3)
    menu()