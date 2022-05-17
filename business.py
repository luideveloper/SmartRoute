# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

def read_employee():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT name, cpf, user, office FROM users;"
    cursor.execute(cod_query_read)
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
    print("Ainda em desenvolvimento")

def remove_account():
    print("Ainda em desenvolvimento")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]