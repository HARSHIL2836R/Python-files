#Write a program to Find the largest/smallest number in a list.

def list_formation():
    global list
    list = []
    n = int(input("Enter number of integers in the list:- "))
    for i in range(1, n+1):
        print("Element ", i, ":- ",end='')
        el = int(input())
        list.append(el)
    print("The list is:- ", list, "\n")
list_formation()

list.sort(reverse=False)
print("Minimum number in the list is:- ", list[0])
list.sort(reverse=True)
print("Maximum number in the list is:- ", list[0])