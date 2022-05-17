# Start - Code written by Erik Dias - [Github: https://github.com/erikdias7]

import sqlite3
import time


def register_vehicles():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    plate = input("Digite a placa do veículo: ")
    type = input("Digite o tipo do veículo: ")
    type = type.upper()
    model = input("Digite o modelo do veículo: ")
    model = model.upper()
    date = input("Digite a data de fabricação do veículo: ")
    km_initial = ("Digite o quilômetro inicial")
    km_now = input("Digite o quilômetro atual: ")
    consultaInsert = "INSERT INTO vehicles (plate,vehicles_type,model,date,km_initial,km_now) VALUES (?,?,?,?,?);"
    cursor.execute(consultaInsert,(plate,type,model,date,km_initial,km_now))
    con.commit()
    con.close()


def read_vehicles():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    query = "SELECT plate, vehicle_type, model, date, km_initial, km_now FROM vehicles;"
    cursor.execute(query)
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
    plate1 = input("Qual placa você quer atualizar? ")
    newplate = input("Nova placa: ")
    typevehicle_newkm = input("Qual veículo vc deseja atualizar o quilômetro? ")
    newkm = input("Qual a quilometragem atual? ")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE cliente SET newplate=?, typevehicle_newkm=?, newkm=?, WHERE plate1=?"
    cursor.execute(consultaAtualizar,(newplate,typevehicle_newkm,newkm,plate1))
    con.commit()
    con.close()


def remove_vehicles():
    read_vehicles()
    plate = int(input("Qual placa do veículo você deseja remover? "))
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consulteDelete = "DELETE FROM vehicle WHERE plate ="
    cursor.execute(consulteDelete+str(plate))
    con.commit()
    con.close()


def trafic_ticket():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    plate_ = input("Qual a placa do veículo? ")
    ticket_hour = input("Qual hora a multa foi feita? ")
    route = input("Qual foi a rota em que o motorista foi mutado")
    route = route.upper()
    driver_name = input("Nome do motorista:")
    driver_name = driver_name.upper()
    ticketadd = "INSERT INTO vehicles (plate_,ticket_hour,route,driver_name) VALUES (?,?,?,?);"
    cursor.execute(ticketadd+str(plate_,ticket_hour,route,driver_name))
    con.commit()
    con.close()

# End - Code written by Erik Dias - [Github: https://github.com/erikdias7]