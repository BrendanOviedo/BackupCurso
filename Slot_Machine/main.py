import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#Canitdad de letras que hay de cada uno
symbol_count = {
    "A" : 6,
    "B" : 6,
    "C" : 6,
    "D" : 6
}

#Valores de multiplicacion dependeidendo de la row que se logre
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

#Se define la funcion con requisitos de parametros, siendo "Simbolos en columnas, Cantidad de lineas, Apuesta, Valores"
def check_winnings(columns, lines, bet, values):
    winnings = 0 #Se inicia con cero ganacias
    winning_lines = [] #cuando se consigue una linea completa esta lista contiene la linea ganadora sea 1 - MAX_LINES
    for line in range(lines): #Se itera cada linea segun la cantidad de lineas
        symbol = columns[0][line] #Se revisa laa posicion cero de cada columna por linea
        for column in columns: #Se define column para iterar por los simbolos del juego
            symbol_to_check = column[line] #Se general la variable en la que se almacena la posicion del simbolo
            if symbol != symbol_to_check: #Si el simbolo es distinto al simbolo anterior se rompe el bucle
                break
        else: #si el bucle for se ejecuta por completo se activa el else, por for/else, de no ser el casi y no se completa el for no se ejecuta else
            winnings += values[symbol] * bet #Se suma a winnings el valor de multiplicacion multiplicado por el valor de la apuesta
            winning_lines.append(line + 1) #Se entrega la linea ganadora, se suma un 1 por que la primera linea es 0 

    return winnings, winning_lines #Se retorna las ganacias despues de haber sumado la ganacia en el juego y se retornan las lineas ganadoras

def get_slot_machine_spin(rows, cols, symbols): #Funcion para conseguir los simbolos de los slots
    
    all_symbols = [] #Lista vacia para guardar los simbolos generados
    for symbol, symbol_count in symbols.items(): # se ejecuta un bucle for que entrega dos valores, el primero siendo el simbolo en si y el segundo es la posicion en la que se encuentra el simbolo
        for _ in range(symbol_count): #Se crea una variable temportal para iteral en la lista 
            all_symbols.append(symbol) #Se inserta en la lista vacia de all_symbols cada simbolo generado
            
    columns = [] 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns    
        
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()        

def deposit():
    while True:
        amount = input("What would you like to deposit?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print(f"Please enter a number 1 - {MAX_LINES}.")
    return lines  

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def game(balance):
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines
        
            if total_bet > balance:
                    print(f"You dont have enought to bet that amount. Your current balance is {balance}")
            else:
                break
        
        print(f"You are betting ${bet} on lines {lines}. Total bet is equal to: ${total_bet}")
    
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
        if winnings > 0:
            print(f"You won ${winnings}!")
            print(f"You won on:", *winnings_lines)
        else:
            print(f"You lost ${total_bet}")
        
        return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        else:
            balance += game(balance)
    print(f"you left with ${balance}")
    
main()