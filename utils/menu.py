from time import sleep

from system import login, create_account, recovery_account, exit, invalid_option, value_error_input

def menu():
    print("\x1b[2J\x1b[1;1H")
    print("=== BEM VINDO AO SMART ROUTE ===")
    print("\n[ 1 ] Faça login")
    print("[ 2 ] Criar conta")
    print("[ 3 ] Recuperar conta")
    print("[ 4 ] Sair do programa")

    try:
        option = int(input("\nO que você deseja? "))

        if (option == 1):
            login()
        elif (option == 2):
            create_account()
        elif (option == 3):
            recovery_account()
        elif (option == 4):
            print("\x1b[2J\x1b[1;1H")
            exit()
        else:
            invalid_option()
            sleep(2)
            menu()
    
    except ValueError:
        value_error_input()