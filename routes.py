# Start - Code written by José Gabriel - [Github: https://github.com/brak3]
#Tabelas para uso, chave_primeira = reg
#                  inicio da rota = route_start
#                  paradas = stop_1, stop_2
#                  final da rota = route_end
#Notas:
#Menu de escolha se vai ou não adicionar paradas ou se so tera inicio e fim FEITO!
#Loopar esse menu caso o usuário digite um valor invalido
#Procurar uma forma de fazer funcionar o update, quando exitir paradas e quando não exitir
#Talvez adicionar algo para a quilometragem, !!! Teria que interagir com um arquivo no excel feito por Rafael !!!
import sqlite3
import time

def create_routes():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    option = int(input("\nDeseja adicionar alguma parada na rota? \n(1)Sim, uma parada \n(2)Sim, duas paradas \n(3)Não"))
    if (option == 3):
        reg = int(input("Informe o código da rota (!Somente números!"))
        route_start = input("Informe o inicio da rota")
        route_start = route_start.upper()
        route_end = input("Informe o destino final da rota")
        route_end = route_end.upper()
        table_insert = "INSERT into routes (reg, route_start, route_end) values (?, ?, ?);"
        cursor.execute(table_insert,(reg, route_start, route_end))
        con.commit()
        con.close()
    
    elif (option == 2):
        reg = int(input("Informe o código da rota (!Somente números!"))
        route_start = input("Informe o inicio da rota")
        route_start = route_start.upper()
        stop_1 = input("Informe a primeira parada")
        stop_1 = stop_1.upper()
        stop_2 = input("Informe a segunda parada")
        stop_2 = stop_2.upper()
        route_end = input("Informe o destino final da rota")
        route_end = route_end.upper()
        table_insert = "INSERT into routes (reg, route_start, stop_1, stop_2, route_end) values (?, ?, ?, ?, ?;)"
        cursor.execute(table_insert,(reg, route_start, stop_1, stop_2, route_end))
        con.commit()
        con.close()

    elif (option == 1):
        reg = int(input("Informe o código da rota (!Somente números!"))
        route_start = input("Informe o inicio da rota")
        route_start = route_start.upper()
        stop_1 = input("Informe a primeira parada")
        stop_1 = stop_1.upper()
        route_end = input("Informe o destino final da rota")
        route_end = route_end.upper()
        table_insert = "INSERT into routes (reg, route_start, stop_1, route_end) values (?, ?, ?, ?;)"
        cursor.execute(table_insert,(reg, route_start, stop_1, route_end))
        con.commit()
        con.close()

def read_routes():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    query = "SELECT reg, route_start, stop_1, stop_2, route_end FROM route;"
    cursor.execute(query)
    print("\n Rotas existentes no sistema: ")
    for linha in cursor.fetchall():
        print("Inicio: ", linha[0])
        print("Primeira parada: ", linha[1])
        print("Segunda parada: ", linha[2])
        print("Destino: ", linha[3])
    con.commit()
    con.close
    
def update_routes():
    print("em desenvolvimento")

def remove_routes():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    read_routes()
    reg = int(input("Qual rota você deseja remover. "))
    tables_delete = "DELETE FROM routes WHERE reg ="
    cursor.execute(tables_delete+str(reg))
    con.commit()
    con.close()


# End - Code written by José Gabriel - [Github: https://github.com/brak3]