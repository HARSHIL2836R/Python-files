import play
import BorB
import host
print('''
                        HAND CRICKET
''')
print('''
                        COIN TOSS
''')
           
def __init__():
    c = int(input("Head(0) or Tail(1)?\t"))
    if c == 0 or 1:
        if BorB._win_lose_() != c:
            print('''

                        You Lose!

            ''')
            BorB._lose_()
        else:
            print('''

                        You Win!

            ''')
            BorB._win_()
    else:
        print("Enter 0 or 1 only!")
        __init__()
__init__()