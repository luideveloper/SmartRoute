# Start - Code written by Lui Richard - [Github: https://github.com/luideveloper]

import sqlite3
import time

from create_bd import *
from menus import *
from accounts import *
from driver import *
from vehicles import *
from routes import *


def start():
    start_bd()
    menu_login()
    
def invalid_option():
     print("Você digitou uma opção inválida")

# End - Code written by Lui Richard - [Github: https://github.com/luideveloper]