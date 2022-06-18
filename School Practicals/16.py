#Write a Program to find frequencies of all elements of a list. Also, print the list of unique elements in the list and duplicate elements in the given list.

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
list2 = []
list3 = []
list_n = []

for i in list:
    if i not in list_n:
        freq = list.count(i)
        print("The frequency of ", i, " in the given list is:- ", freq)
        if freq == 1:
            list2.append(i)
        elif freq == 2:
            if i not in list3:
                list3.append(i)
        list_n.append(i)
    else:
        continue

print("\nThe unique elements in the list are:- ", list2)
print("\nThe duplicate elements in the list are:- ", list3)