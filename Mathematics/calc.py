print("""
    In this calculator only one operator separated by a blank space can be used.
    """)   
def add():
    ml = input("Calculator - ")
    #convert strings to list
    r = ml.split()
    if len(r) == 3:
        if ml.find(' ') != -1:
            if ml.find('+') != -1:
                # print(r)
                r.remove('+')
                # convert string numbers to integers
                mlr = map(int, r)
                intmlr = list(mlr)
                # print(intmlr)
                eq = sum(intmlr)
                print('=', eq)
        else:
            print("Whitespace required")

    else:
        print("Error in statement")
add()
