# Write a Program to count the frequency of list
# elements using a dictionary.

# Forming List
n = int(input('Enter number of elements in list:- '))
li = list()
for i in range(n):
    li.append(int(input('Enter element %d:-'%(i+1))))

dic = dict()

for el in li:
    dic[el] = li.count(el)

print("Frequencies of elements is:- ")
print(str(dic))