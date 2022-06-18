import random
import play
import host
def _win_lose_():
    return random.randint(0,1)

def _win_():
    x = int(input("Do you want to Bat(0) or Bowl(1)?\t"))
    if x == 0:
        print("Time to bat")
        play.batting()

    elif x == 1:
        print("Time to bowl")
        play.bowling()

    else:
        print("Enter 0 or 1 only!")
        BorB._win_()

def _lose_():
    if random.randint(0,1) == 0:
        print('''

                        SYSTEM CHOSES TO BALL                        

        ''')
        play.batting()
    else:
        print('''

                        SYSTEM CHOSES TO BAT                        

        ''')
        play.bowling()