#bloco iniciado por erik dias 

import sqlite3

def register():
    con = sqlite3.connect('dados.db')
    cursor = con.cursor()
    vehicles_type = input("Digite o tipo do veículo: ")
    model = input("Digite o modelo do veículo: ")
    date = input("Digite a data de fabricação do veículo: ")
    km_initial = input("Digite o quilômetro inicial: ")
    km_now = input("Digite o quilômetro atual: ")
    consultaInsert = "INSERT INTO vehicles (vehicles_type,model,date,km_initial,km_now) VALUES (?,?,?,?,?);"
    cursor.execute(consultaInsert,(vehicles_type,model,date,km_initial,km_now))
    con.commit()
    con.close()
#bloco fechado por erik dias 