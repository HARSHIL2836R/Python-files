#Write a program to Input a tuple of elements, search for a given element in the tuple.

def list_formation():
    global list
    list = []
    n = int(input("Enter number of elements in the tuple:- "))
    for i in range(1, n+1):
        print("Element ", i, ":- ",end='')
        el = input()
        list.append(el)
    print("The tuple is:- ", list)
list_formation()

tup = tuple(list)
x = input("The element you want to search:- ")
if x in tup:
    i = tup.index(x)
    if i != -1:
        print("The element is at ", i, "position.")
else:
    print("The element is not in the given list.")