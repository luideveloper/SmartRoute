# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

def register_driver():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    print("\n=== CADASTRO NOVO MOTORISTA ===\n")
    name = input("Nome: ")
    cpf = input("CPF: ")
    type_license = input("Categoria da Habilitação: ")
    validity_license = input("Validade da Habilitação: ")
    cod_query_creat = "INSERT INTO driver (name,cpf,type_license,validity_license) VALUES (?,?,?,?);"
    cursor.execute(cod_query_creat,(name,cpf,type_license,validity_license))
    con.commit()
    print("\n>> MOTORISTA CADASTRADO COM SUCESSO <<")
    time.sleep(3)
    con.close()

def read_driver():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_read = "SELECT name, cpf, type_license, validity_license FROM driver;"
    cursor.execute(cod_query_read)
    print("\n== MOTORISTAS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("Nome:", linha[0])
        print("CPF:", linha[1])
        print("Categoria da Habilitação:", linha[2])
        print("Validade da Habilitação:", linha[3])
        print("\n-------------------")
    time.sleep(3)
    con.close()

def update_driver():
    print("\x1b[2J\x1b[1;1H")
    cpf = input("\nQual o cpf do motorista que deseja atualizar os dados? ")
    print("\n=== DIGITE OS DADOS ATUALIZADOS ===\n")
    new_name = input("Nome: ")
    new_cpf = input("CPF: ")
    new_type_license = input("Categoria da Habilitação: ")
    new_validity_license = input("Validade da Habilitação: ")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_update = "UPDATE driver SET name=?, cpf=?, type_license=?, validity_license=? WHERE cpf=?"
    cursor.execute(cod_query_update,(new_name,new_cpf,new_type_license,new_validity_license,cpf))
    con.commit()
    print("\n>> MOTORISTA ATUALIZADO COM SUCESSO <<")
    time.sleep(3)
    con.close()

def remove_driver():
    print("\x1b[2J\x1b[1;1H")
    read_driver()
    cpf = int(input("\nQual o cpf do motorista que deseja remover? "))
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    cod_query_remove = "DELETE FROM driver WHERE cpf ="
    cursor.execute(cod_query_remove+str(cpf))
    con.commit()
    print("\n>> MOTORISTA REMOVIDO COM SUCESSO <<")
    time.sleep(3)
    con.close()

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]