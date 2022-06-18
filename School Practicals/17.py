# Write a program to Input a list of numbers and swap elements at the even location with the elements at the odd location.

def list_formation():
    global list
    list = []
    n = int(input("Enter number of elements in the list:- "))
    for i in range(1, n+1):
        print("Element ", i, ":- ",end='')
        el = input()
        list.append(el)
    print("The list is:- ", list)
list_formation()

for i in range(0, len(list)+1):
    if i % 2 == 0:
        temp = list[i]
        list.pop(i)
        list.insert(i+1, temp)

print("\nList with elements at even location swapped with elements at odd location:- ", list)
