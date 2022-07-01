# Aqui é a área de veículos do Smart Route

# Importação de bibliotecas ↓

import sqlite3
import time

# Área de funções ↓

# Função de cadastro contém as variáveis: (plate,type,model,date,km_initial,km_now) ↓

def register_vehicles():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("SmartRoute\database\dados.db") 
    cursor = con.cursor()
    plate = input("\nPlaca do veículo: ")
    plate = plate.upper()
    vehicles_type = input("Tipo do veículo: ")
    model = input("Modelo do veículo: ")
    date = input("Ano de fabricação do veículo: ")
    km_initial = input("Quilômetro inicial: ")
    km_now = input("Quilômetro atual: ")
    consultaInsert = "INSERT INTO vehicles (plate,vehicles_type,model,date,km_initial,km_now) VALUES (?,?,?,?,?,?);"
    cursor.execute(consultaInsert,(plate,vehicles_type,model,date,km_initial,km_now))
    con.commit()
    print("\n>> VEÍCULO CADASTRADO COM SUCESSO <<")
    time.sleep(3)
    con.close()

# Função de leitura apenas apresenta todos os veículos cadastrados e suas informações ↓

def read_vehicles():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("SmartRoute\database\dados.db")
    cursor = con.cursor()
    query = "SELECT plate, vehicles_type, model, date, km_initial, km_now FROM vehicles;"
    cursor.execute(query)
    print("\x1b[2J\x1b[1;1H")
    print("\n== VEÍCULOS CADASTRADOS ==")
    for linha in cursor.fetchall():
        print("\nPlaca:", linha[0])
        print("Tipo:", linha[1])
        print("Modelo:", linha[2])
        print("Data:", linha[3])
        print("Quilômetro inicial:", linha[4])
        print("Quilômetro atual:", linha[5])
        print("\n-------------------")
    con.commit()
    time.sleep(8)
    con.close()

# Função de atualização contém as variáveis: (plate,newplate,km_now) ↓

def update_vehicles():
    print("\x1b[2J\x1b[1;1H")
    plate = input("Qual placa do veículo que você deseja atualizar? ")
    plate = plate.upper()
    print("\x1b[2J\x1b[1;1H")
    newplate = input("Placa do veículo: ")
    newplate = newplate.upper()
    km_now = input("Qual a quilometragem atual: ")
    con = sqlite3.connect("SmartRoute\database\dados.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE vehicles SET plate=?, km_now=? WHERE plate=?"
    cursor.execute(consultaAtualizar,(newplate,km_now,plate))
    con.commit()
    print("\n>> ATUALIZAÇÃO REALIZADA COM SUCESSO <<")
    time.sleep(3)
    con.close()
    
# Função de remoção contém as variáveis (plate) ↓

def remove_vehicles():
    print("\x1b[2J\x1b[1;1H")
    plate = input("Qual placa do veículo você deseja remover? ")
    plate = plate.upper()
    con = sqlite3.connect("SmartRoute\database\dados.db")
    cursor = con.cursor()
    consulteDelete = "DELETE FROM vehicles WHERE plate=?"
    cursor.execute(consulteDelete,(plate,))
    con.commit()
    print("\n>> REMOÇÃO REALIZADA COM SUCESSO <<")
    time.sleep(3)
    con.close()
 
