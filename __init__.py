import random
import colorama
from colorama import Fore
colorama.init()
INDEX_GAME='y'
WIN_COUNTER=0
LOSE_COUNTER=0
TIE_COUNTER=0
def play():
    global INDEX_GAME
    user=input("please enter your choice: R for rock, P for paper, S for scissors: ")
    user_key=check_valid_input(user.lower())
    computer=random.choice(['r','p','s'])
    result_game_statuse(computer,user_key)
    INDEX_GAME=input("for another game press y else press any key: ").lower()

def check_valid_input(key):
    while((key!='r') or (key!='p') or (key!='s')):
        if ((key.lower() == 'r') or (key.lower() == 'p') or (key.lower() == 's')):
            return key.lower()
        else:
            key=input("WORNG LETTER. \nR for rock, P for paper, S for scissors: ")
    return key.lower()

def win(player,computer):
    if((player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r')):
        return True
def result_game_statuse(computer,key):
    global WIN_COUNTER
    global LOSE_COUNTER
    global TIE_COUNTER
    print("the computer choose is: ", computer)
    if (key == computer):
        TIE_COUNTER += 1
        print(Fore.YELLOW + "IT'S A TIE\n", '\033[39m')
        #print("IT'S A TIE\n", '\033[39m')
    elif (win(key, computer)):
        WIN_COUNTER += 1
        print(Fore.BLUE + "YOU WIN\n", '\033[39m')
        #print("YOU WIN\n", '\033[39m')
    else:
        LOSE_COUNTER += 1
        print(Fore.RED + "YOU LOST\n", '\033[39m')
        #print("YOU LOST\n", '\033[39m')
    print("amount of WIN: ", WIN_COUNTER, " amount of LOSE: ", LOSE_COUNTER, " amount of TIE: ", TIE_COUNTER)

def main():

    while INDEX_GAME=='y':
        play()
    print("\nTHANKS FOR PLAYING! SEE YOU NEXT TIME :)")
if __name__ == "__main__":
    main()
