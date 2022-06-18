#Write a Program to find frequencies of all elements of a list. Also, print the list of unique elements in the list and duplicate elements in the given list.
import collections

def list_formation():
    list = []
    n = int(input("Enter number of integers in the list:- "))
    for i in range(1, n+1):
        print("Element ", i, ":- ",end='')
        el = int(input())
        list.append(el)
    print("The list is:- ", list)
list_formation()

print("Frequency of the elements in the List : ", collections.Counter(list))