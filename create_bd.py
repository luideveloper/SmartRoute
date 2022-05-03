import sqlite3
from os import system
from system import *
from accounts import *
from driver import *
from vehicles import *
from routes import *

def start_bd():
    con = sqlite3.connect('SmartRoute/dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS driver (reg integer not null, name VARCHAR(200), cpf VARCHAR(11), type_license VARCHAR(100), validity_license VARCHAR(100), PRIMARY KEY (reg));")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (codigo integer, marca VARCHAR(200), modelo VARCHAR(200), data_fabricação VARCHAR(200), km_atual VARCHAR(200), ultima_km_manutencao VARCHAR(200));")
    cursor.execute("CREATE TABLE IF NOT EXISTS routes (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id integer not null, user VARCHAR(200), password VARCHAR(200), security_key VARCHAR(100), PRIMARY KEY (id));")
    con.commit()
    con.close()
    full_menu()

def con():
    con = sqlite3.connect('SmartRoute/dados.db')
