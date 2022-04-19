# bloco iniciado por lui richard

import sqlite3

def start():
    con = sqlite3.connect('dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (codigo integer, marca VARCHAR(200), modelo VARCHAR(200), data_fabricação VARCHAR(200), km_atual VARCHAR(200), ultima_km_manutencao VARCHAR(200));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    con.commit()
    con.close()

def menu():
    print("\nOlá, seja bem vindo ao Smart Route, o que você deseja?\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas\n")

def invalid_option():
     print("Você digitou uma opção inválida")

# bloco fechado por lui richard