import random
# -------- # Funcion para elegir------------
def select_options():

    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
      print('esa opcion no es valida')
    
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option
# --------- # Funcion para las reglas del juego ---------------------
def rules_game(user_option, computer_option,user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    return user_wins, computer_wins
#  ------------ Funcion Para verificar el ganador ---------------
def check_winner(user_wins,computer_wins):
    if computer_wins == 2:
        print('El ganador es la computadora')
        
    if user_wins == 2:
        print('El ganador es el usuario')     
#  -------------Funcion que inicia el juego --------------
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1
        
#----------- aqui se selecciona la opcion------------
    # print('*' * 10)
    # print('ROUND', rounds)
    # print('*' * 10)

    # print('computer_wins', computer_wins)
    # print('user_wins', user_wins)

    # user_option = input('piedra, papel o tijera => ')
    # user_option = user_option.lower()

    # rounds += 1

    # if not user_option in options:
    #   print('esa opcion no es valida')
    #   continue

    # computer_option = random.choice(options)

    # print('User option =>', user_option)
    # print('Computer option =>', computer_option)
# ------------aqui se checan las reglas del juego ---------
        user_option, computer_option = select_options()

# ------------- #funcion de selecionar-----------
        user_wins, computer_wins = rules_game(user_option, computer_option, user_wins, computer_wins)
        
#------------------- #funcion contador de ganador -----------------
        check_winner()
        # if computer_wins == 2:
        #     print('El ganador es la computadora')
        #     break

        # if user_wins == 2:
        #     print('El ganador es el usuario')
        #     break
# -------- se llama a la funcion Para que inicie el juego ------------
run_game()

