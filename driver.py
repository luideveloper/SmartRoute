# bloco iniciado por lui richard

import sqlite3

def register_driver():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    print("\n=== CADASTRO NOVO MOTORISTA ===\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    codigo_plano = int(input("Código Plano: "))
    consultaInsert = "INSERT INTO driver (nome,cpf,email,codigo_plano) VALUES (?,?,?,?);"
    cursor.execute(consultaInsert,(nome,cpf,email,codigo_plano))
    con.commit()
    con.close()

def read_driver():
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consulta = "SELECT nome, cpf, email, codigo_plano FROM cliente;"
    cursor.execute(consulta)
    print("\n== CLIENTES CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("Nome", linha[0])
        print("CPF:", linha[1])
        print("E-mail:", linha[2])
        print("Código do plano:", linha[3])
        print(" -------------------")

    con.close()   

def update_driver():
    cpf = input("Qual o cpf do cliente a atualizar? ")
    novoNome = input("Nome: ")
    novoCPF = input("CPF: ")
    novoEmail = input("Email: ")
    novoCodigoPlano = input("Codigo Plano: ")
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE cliente SET nome=?, cpf=?, email=?, codigo_plano=? WHERE cpf=?"
    cursor.execute(consultaAtualizar,(novoNome,novoCPF,novoEmail,novoCodigoPlano,cpf))
    con.commit()
    con.close()

def remove_driver():
    read_driver()
    cpf = int(input("Qual o cpf do cliente a remover? "))
    con = sqlite3.connect("dados.db")
    cursor = con.cursor()
    consultaDelete = "DELETE FROM cliente WHERE cpf ="
    cursor.execute(consultaDelete+str(cpf))
    con.commit()
    con.close()

# bloco fechado por lui richard