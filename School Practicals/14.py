# Write a Program to calculate mean of a given list of numbers.

def list_formation():
    global list, n
    list = []
    n = int(input("Enter number of integers in the list:- "))
    for i in range(1, n+1):
        print("Element ", i, ":- ",end='')
        el = int(input())
        list.append(el)
    print("The list is:- ", list)

list_formation()
mean = sum(list)/n
print("The mean of given list of numbers is:- ", mean)