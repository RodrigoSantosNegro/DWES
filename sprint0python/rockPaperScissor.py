import random

machineScore = 0
playerScore = 0

#Escribiremos un método para comprobar o gañador en cada xogada. En caso de empate devolverase 'Tie'
def play(machineChoice, playerChoice):
    if(machineChoice == 'Rock' and playerChoice == 'Paper'):
        return playerChoice
    elif(machineChoice == 'Rock' and playerChoice == 'Scissor'):
        return machineChoice
    elif(machineChoice == 'Paper' and playerChoice == 'Rock'):
        return machineChoice
    elif(machineChoice == 'Paper' and playerChoice == 'Scissor'):
        return playerChoice
    elif(machineChoice == 'Scissor' and playerChoice == 'Rock'):
        return playerChoice
    elif(machineChoice == 'Scissor' and playerChoice == 'Paper'):
        return machineChoice
    else:
        return 'Tie'
#contador de xogadas totales
plays = 0
while(plays < 5):
    #Facemos unha pequena lista coas posibles opcións
    machine = ['Rock', 'Paper', 'Scissor']

    print("""¿What are you going to play?
        1) Rock
        2) Paper
        3) Scissor
        """)
    selection = False
    while(selection == False):
        playerChoice = input('Your hand: ')
        if(playerChoice == '1' or playerChoice.lower == 'rock'):
            playerChoice = 'Rock'
            selection = True
        elif(playerChoice == '2' or playerChoice.lower == 'paper'):
            playerChoice = 'Paper'
            selection = True
        elif(playerChoice == '3' or playerChoice.lower == 'scissor'):
            playerChoice = 'Scissor'
            selection = True
        else:
            print('You must write what you want to play (rock, paper or scissor) or write the left number on the menu')
    #Collemos unha opción aleatoria da lista e mostrámola en maiúsculas xunto co gañador (e unha posible frase se se dan as condicións)
    machineChoice = random.choice(machine)
    print('Okey, so i\'m going to play ', machineChoice.upper(),'\n')
    if(play(machineChoice, playerChoice) == machineChoice):
        plays += 1
        print('The machine ',machineChoice.upper(), ' defeat player ', playerChoice.upper())
        if(machineScore>1):
            print('*Machine*: You have nothing to do against me haha')
        machineScore += 1
    elif(play(machineChoice, playerChoice) == playerChoice):
        plays += 1
        print('The machine ',machineChoice.upper(), ' losses player ', playerChoice.upper())
        if(machineScore<2 and plays > 2):
            print('*Machine*: shit, your good at this')
        playerScore += 1
    else:
        print(machineChoice.upper(), 'vs', playerChoice.upper(), '\nThats a tie!! Try it again')
    print('\n--------------------------')
    print('Machine score: ', machineScore)
    print('Player score: ', playerScore)
    print('--------------------------\n')

if(playerScore == 3):
    winner = 'theeee handsoome Plaayeeer!'
else:
    winner = 'the Ultimate Machine!'
print('And the winner is.............', winner,'\n')