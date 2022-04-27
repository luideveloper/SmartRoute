#bloco iniciado por erik dias 

import sqlite3

def register():
    con = sqlite3.connect('dados.db')
    cursor = con.cursor()
    plate = input("Digite a placa do veículo: ")
    vehicles_type = input("Digite o tipo do veículo: ")
    model = input("Digite o modelo do veículo: ")
    date = input("Digite a data de fabricação do veículo: ")
    km_now = input("Digite o quilômetro atual: ")
    consultaInsert = "INSERT INTO vehicles (plate,vehicles_type,model,date,km_initial,km_now) VALUES (?,?,?,?,?);"
    cursor.execute(consultaInsert,(plate,vehicles_type,model,date,km_now))
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
#bloco fechado por erik dias 