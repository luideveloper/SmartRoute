import sqlite3

def start():
    con = sqlite3.connect('dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS motorista (id integer not null, nome VARCHAR(200), cpf VARCHAR(11), email VARCHAR(100), codigo_plano integer, PRIMARY KEY (id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS veiculos (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    cursor.execute("CREATE TABLE IF NOT EXISTS rotas (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    cursor.execute("CREATE TABLE IF NOT EXISTS plano (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    con.commit()
    con.close()

def menu():
    print("\nOlá, seja bem vindo ao Smart Route, o que você deseja?\n")
    print("[ 1 ] Acessar área dos motoristas")
    print("[ 2 ] Acessar área dos veículos")
    print("[ 3 ] Acessar área de rotas\n")

def invalid_option():
     print("Você digitou uma opção inválida")