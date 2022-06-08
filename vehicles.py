#>Start - Code written by Erik Dias - [Github: https://github.com/erikdias7]<
#---------------------------------------------------------------------------------------------------------------------------------------
#>Aqui é a área de veículos do Smart Route<
#---------------------------------------------------------------------------------------------------------------------------------------
#>Função de cadastro contém as variáveis: (plate,type,model,date,km_initial,km_now)<
#---------------------------------------------------------------------------------------------------------------------------------------
#>Função de leitura apenas apresenta todos os veículos cadastrados e suas informações<
#---------------------------------------------------------------------------------------------------------------------------------------
#>Função de atualização contém as variáveis: (plate,newplate,km_now)<
#---------------------------------------------------------------------------------------------------------------------------------------
#>Função de remoção contém as variáveis> (plate)>
#---------------------------------------------------------------------------------------------------------------------------------------
#>Área de importação<
#---------------------------------------------------------------------------------------------------------------------------------------
import sqlite3
import time
#---------------------------------------------------------------------------------------------------------------------------------------
#>Área de funções<
#---------------------------------------------------------------------------------------------------------------------------------------
def register_vehicles():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    print("\n>> Olá, bem vindo a área de cadastro de veículos <<")
    plate = input("Digite a placa do veículo: ")
    plate = plate.upper()
    print("\x1b[2J\x1b[1;1H")
    type = input("Digite o tipo do veículo: ")
    type = type.upper()
    print("\x1b[2J\x1b[1;1H")
    model = input("Digite o modelo do veículo: ")
    model = model.upper()
    print("\x1b[2J\x1b[1;1H")
    date = input("Digite a data de fabricação do veículo: ")
    print("\x1b[2J\x1b[1;1H")
    km_initial = input("Digite o quilômetro inicial: ")
    print("\x1b[2J\x1b[1;1H")
    km_now = input("Digite o quilômetro atual: ")
    print("\x1b[2J\x1b[1;1H")
    consultaInsert = "INSERT INTO vehicles (plate,vehicles_type,model,date,km_initial,km_now) VALUES (?,?,?,?,?,?);"
    cursor.execute(consultaInsert,(plate,type,model,date,km_initial,km_now))
    con.commit()
    print("\n>> CADASTRADO REALIZADO COM SUCESSO, INICIE O SISTEMA NOVAMENTE PARA CONTINUAR <<")
    con.close()


def read_vehicles():
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    query = "SELECT plate, vehicles_type, model, date, km_initial, km_now FROM vehicles;"
    cursor.execute(query)
    print("\x1b[2J\x1b[1;1H")
    print("\n== VEÍCULOS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("Placa:", linha[0])
        print("Tipo:", linha[1])
        print("Modelo:", linha[2])
        print("Data:", linha[3])
        print("Quilômetro inicial:", linha[4])
        print("Quilômetro atual:", linha[5])
        print(" -------------------")
    con.commit()
    con.close()


def update_vehicles():
    print("\x1b[2J\x1b[1;1H")
    print("\n>> Olá, bem vindo a área de atualização de veículos <<")
    plate = input("Qual placa você quer atualizar? ")
    plate = plate.upper()
    print("\x1b[2J\x1b[1;1H")
    newplate = input("Nova placa: ")
    newplate = newplate.upper()
    print("\x1b[2J\x1b[1;1H")
    km_now = input("Qual a quilometragem atual? ")
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE vehicles SET plate=?, km_now=? WHERE plate=?"
    cursor.execute(consultaAtualizar,(newplate,km_now,plate))
    con.commit()
    print("\n>> ATUALIZAÇÃO REALIZADA COM SUCESSO, INICIE O SISTEMA NOVAMENTE PARA CONTINUAR <<")
    con.close()
    

def remove_vehicles():
    print("\x1b[2J\x1b[1;1H")
    print("\n>> Olá, bem vindo a área de remoção de veículos <<")
    plate = input("Qual placa do veículo você deseja remover? ")
    plate = plate.upper()
    print("\x1b[2J\x1b[1;1H")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consulteDelete = "DELETE FROM vehicles WHERE plate=?"
    cursor.execute(consulteDelete,(plate,))
    con.commit()
    print("\n>> REMOÇÃO REALIZADA COM SUCESSO, INICIE O SISTEMA NOVAMENTE PARA CONTINUAR <<")
    con.close()
#---------------------------------------------------------------------------------------------------------------------------------------
#>End - Code written by Erik Dias - [Github: https://github.com/erikdias7]<