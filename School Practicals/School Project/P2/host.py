import BorB
import play
def bat_first():
        #GETTING RUNS MADE BY USER
        r1 = play.bat_r[0]
        print("Time to bowl")
        play.bowling(2)
        #GETTING RUNS MADE BY COMPUTER
        r2 = play.bowl_r[0]
        if r1 > r2:
            print('''
                    YOU WIN!!
            ''')
        elif r1 < r2:
            print('''
                    YOU LOSE!!
            ''')
        elif r1 == r2:
            print('''
                    THE MATCH TIED!!
            ''')
def bowl_first():
        #GETTING RUNS MADE BY COMPUTER
        r2 = play.bowl_r[0]
        print("Time to bat")
        play.batting()
        #GETTING RUNS MADE BY USER
        r1 = play.bat_r[0]
        if r1 > r2:
            print('''
                    YOU WIN!!
            ''')
        elif r1 < r2:
            print('''
                    YOU LOSE!!
            ''')
        elif r1 == r2:
            print('''
                    THE MATCH TIED!!
            ''')