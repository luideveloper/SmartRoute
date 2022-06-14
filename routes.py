# Start - Code written by José Gabriel - [Github: https://github.com/brak3]

# Uso na tabela: chave_primeira = reg
#                  inicio da rota = route_start
#                  paradas = stop_1
#                  paradas = stop_2 
#                  final da rota = route_end

# Importação de bibliotecas ↓

import sqlite3
import time

# Criação de rotas ↓

def create_routes():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()

    cod_query_read = "SELECT route_code FROM routes"
    cursor.execute(cod_query_read)

    list_route_code = []

    for linha in cursor.fetchall():
        route_code_bd = linha[0]
        list_route_code.append(route_code_bd)

    print("A rota irá ter paradas? ")
    print("\n[ 1 ] Sim")
    print("[ 2 ] Não")
    option = int(input("\nQual das opções? "))

    if (option == 1):
        print("\x1b[2J\x1b[1;1H")
        route_code = int(input("Código da rota: "))
        route_start = input("Ponto inicial da rota: ")
        stop_1 = input("Primeira parada na rota: ")
        stop_2 = input("Segunda parada na rota: ")
        route_end = input("Destino final da rota: ")

        if (route_code in list_route_code):
            print("\x1b[2J\x1b[1;1H")
            print("== Código de rota já existente em cadastro ==")
            print("\n Opções")
            print("[ 1 ] Voltar ao painel de funções")
            print("[ 2 ] Sair do programa")

            option = int(input("\nO que você deseja? "))

            if (option == 1):
                con.close()
            elif (option == 2):
                print("\x1b[2J\x1b[1;1H")
                exit()
        else:
            table_insert = "INSERT into routes (route_code, route_start, stop_1, stop_2, route_end) values (?, ?, ?, ?, ?)"
            cursor.execute(table_insert,(route_code, route_start, stop_1, stop_2, route_end))
            con.commit()
            print("\n>> ROTA CADASTRADA COM SUCESSO <<")
            time.sleep(3)
            con.close()

    elif (option == 2):
        print("\x1b[2J\x1b[1;1H")
        route_code = int(input("Código da rota: "))
        route_start = input("Informe o inicio da rota: ")
        stop_1 = "Não possui paradas."
        stop_2 = "Não possui paradas."
        route_end = input("Informe o destino final da rota: ")

        if (route_code in list_route_code):
            print("\x1b[2J\x1b[1;1H")
            print("== Código de rota já existente em cadastro ==")

            print("\n Opções")
            print("[ 1 ] Voltar ao painel de funções")
            print("[ 2 ] Sair do programa")

            option = int(input("\nO que você deseja? "))

            if (option == 1):
                con.close()
            elif (option == 2):
                print("\x1b[2J\x1b[1;1H")
                exit()
        else:
            table_insert = "INSERT into routes (route_code, route_start, stop_1, stop_2, route_end) values (?, ?, ?, ?, ?)"
            cursor.execute(table_insert,(route_code, route_start, stop_1, stop_2, route_end))
            con.commit()
            print("\n>> ROTA CADASTRADA COM SUCESSO <<")
            time.sleep(3)
            con.close()
    
    else:
        print("\x1b[2J\x1b[1;1H")
        print("== ATENÇÃO ==\n")
        print(">> Opção inválida")
        con.commit()
        time.sleep(3)
        con.close()
    
# Leitura de rotas ↓

def read_routes():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    query = "SELECT route_code, route_start, stop_1, stop_2, route_end FROM routes;"
    cursor.execute(query)
    print("== ROTAS CADASTRADAS ==")
    for linha in cursor.fetchall():
        print("\nCódigo: ", linha[0])
        print("Inicio: ", linha[1])
        print("Primeira parada: ", linha[2])
        print("Segunda parada:  ", linha[3])
        print("Destino final: ", linha[4])
        print("\n-------------------")
    con.commit()
    time.sleep(10)
    con.close

# Atualização de rotas ↓
    
def update_routes():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    route_code = input("Qual o código da rota que você deseja atualizar? ")
    new_route_start = input("\nNovo inicio da rota: ")
    new_stop_1 = input("Nova primeira parada: ")
    new_stop_2 = input("Nova segunda parada :")
    new_route_end = input("Novo destino final da rota: ")
    print("\x1b[2J\x1b[1;1H")
    routes_update = "UPDATE routes SET route_start=?, stop_1=?, stop_2=?, route_end=? WHERE route_code=?"
    cursor.execute(routes_update,(new_route_start,new_stop_1, new_stop_2,new_route_end,route_code))
    con.commit()
    print("\n>> ATUALIZAÇÃO REALIZADO COM SUCESSO <<")
    time.sleep(3)
    con.close()

# Remoção de rotas ↓

def remove_routes():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    route_code = int(input("Qual o código da rota que você deseja? "))
    tables_delete = "DELETE FROM routes WHERE route_code=?"
    cursor.execute(tables_delete,(route_code,))
    con.commit()
    print("\n>> REMOÇÃO REALIZADA COM SUCESSO <<")
    time.sleep(3)
    con.close()


# End - Code written by José Gabriel - [Github: https://github.com/brak3]