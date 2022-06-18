import math as ma


program_running = True



while program_running is True:


    class Variables():


        # Getting the input

        Inp1 = int(input("First Number:-- \n    "))

        Inp2 = int(input("Secod Number:-- \n    "))


        # Defining the function of printing the LCM

        def output(number1 , number2):


            # assigning variable to the call

            lcm = ma.lcm(int(number1) , int(number2))


            # final job!

            print("The LCM of provided numbers is :- "+ '\n    '+ str(lcm) + '\n'+'\n')


        # calling the funtion

        output(Inp1, Inp2)
        
    confirmation = input("Want more LCMs ?(y/n) \n    ")

    print('\n \n')

    if confirmation == "n":

        program_running = False

        break

    else:
        continue
