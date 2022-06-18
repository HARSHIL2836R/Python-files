import matplotlib.pyplot as plt
import numpy as np

def sin(x):
    np.sin(x)
    
print("first enter the range of X accordingly")
(Rx1, Rx2) = (float(input("First value:- ")), float(input("Second Value:- ")))

x = np.arange(Rx1, Rx2, 0.1)

y = input("Please enter the function of x:-   ")

plt.plot(x, y)

plt.show()
