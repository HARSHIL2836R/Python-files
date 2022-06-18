# Create a dictionary with the roll number, name and marks of n students in a class and display the
# names of students who have scored marks above 75.

n = int(input('Enter number of students:-'))
dic = dict()
for i in range(n):
    name = input("Enter name of student %d:- "%(i+1))
    roll = int(input('Enter roll no. of student %s:-'%name))
    marks = int(input('Enter marks of student %s:-'%name))
    dic[name] = [roll, marks]

print("---------------------------------------------------")
print("Students whose marks are above 75 are:- ")
for el in dic.keys():
    if dic[el][1] > 75:
       print(dic[el][0], ".  ",el)
print("----------------------------------------------------")