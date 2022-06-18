# A dictionary contains details of two workers with their names as keys
# and other details in the form of dictionary as value.
# Write a program to print the workers information in records format.

journal = dict()
n = int(input("Enter number of workers:- "))
for i in  range(n):
    name = input("Enter name of worker %d:- "%(i+1))
    age = input("Enter age of %s:- "%name)
    salary = input("Enter salary of %s:- "%name)
    journal[name] = [age,salary]

print("-------------------------------------------------")
print("The Journal looks like:- ")
for el in journal.keys():
    print(el,":-\n")
    print("The age of %s is %s."%(el, journal[el][0]))
    print("The salary of %s is %s."%(el, journal[el][1]))
print("-------------------------------------------------")