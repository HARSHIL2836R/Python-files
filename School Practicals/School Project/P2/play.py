import BorB
import host
#VARIABLES
_range_ = (1,2,3,4,5,6,7,8,9,10) #TUPLE
run = [0]
run_sys = [0]

def choice(l):
    try:
        num1 = int(input("Enter number:- "))
    except:
        print("Enter Numbers only!!!!!!!!!!!!!!!!!!!!!!!")
        if l == 1:
            batting()
        if l == 0:
            bowling()
    
    if num1 in _range_:
        return num1

    else:
        print("ENTER NUMBERS BETWEEN 1 AND 10 ONLY!!!!!!!!!")
        if l == 1:
            batting()
        if l == 0:
            bowling()

def bowling(l):
    num3 = choice(0)
    num4 = 3
    print("System played:- ", num4)
    check_bowl(num3, num4, l)

def batting(l):
    num1 = choice(1)
    num2 = 3
    print("System played:- ", num2)
    check_bat(num1, num2, l)

def check_bat(num1, num2, l):
    global bat_r
    if num1 == num2:
        print('''
            You are out!
            ''')
        print('''
        Your score is %d
        '''%(sum(run)))
        bat_r = (sum(run),)
        host.bat_first()

    elif num1 != num2:
         run.append(num1)
         batting()

def check_bowl(num3, num4):
    global bowl_r
    if num3 == num4:
        print('''
            The System is out!
        ''')
        print('''
        System's score is %d
        '''%(sum(run_sys)))
        bowl_r = (sum(run_sys),)
        host.bowl_first()
        
    elif num3 != num4:
         run_sys.append(num4)
         bowling()
