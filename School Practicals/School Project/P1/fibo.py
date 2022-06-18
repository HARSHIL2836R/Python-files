from Functions import my_fun as mf

###############################################################
print('''
                                FIBONACCI NUMBERS
                    A pattern found in their Digital Roots
''')
print('''
    The digital root (also repeated digital sum) of a natural number in a given radix 
    is the (single digit) value obtained by an iterative process of summing digits,on each 
    iteration using the result from the previous iteration to compute a digit sum.
    For example, for 24867, digital sum is 2 + 4 + 8 + 6 + 7 = 27
    and its digital root is 2+7 = 9
''')
input("\nPress ENTER to continue\n")
###############################################################

###############################################################
sr = mf.my_list().var().sr
li = mf.my_list().var().li
lis = mf.my_list().var().lis

#APPENDING ELEMENTS IN LIST
for i in range(0, 1000):
    sr.append(i)

    prev_el_1 = li[len(li)-1]
    prev_el_2 = li[len(li)-2]
    #Adding element which is sum of prev. 2 elements
    li.append(prev_el_1+prev_el_2)
    
    #Got digital sum
    su = mf.number().digit().get_sum(prev_el_1)
    
    #Getting digital root to single digit
    while su >= 10:
        su = mf.number().digit().get_sum(su)
    
    #Adding digial sum, now acquired, to its list
    lis.append(su)
###############################################################

###############################################################
print('''
    List of Fibonacci Numbers:
    %s ...etc
'''%(mf.my_list().int_list_to_str(li[0:20])))

input("\nPress ENTER to continue\n")
###############################################################


#Creating dictionary with serial number of numbers and the digital root of the fibonacci number
_dict_ = dict(zip(sr, lis))

###############################################################
print('''
    The Digital Roots corresponding to each Fibonacci number are:
''')
mf.dic().print_some_keys(_dict_)
print("\tand so on...")
input("\nPress ENTER to continue\n")
print('''
    We will explore a fact!
    Sum of digital roots between consequtive 9's follow a pattern!!
''')
###############################################################


###############################################################
#Splitting dictionary for the values b/w consecutive 9's

oc = mf.dic().var().occ
c = mf.dic().var().count
# list of digital roots
values = list(_dict_.values())
spl = mf.dic().var().splitted

for i in _dict_.keys():
    #Getting 9
    if _dict_.get(i) == 9:
        oc += (i, )
        #There is 9 at ind1 index in digital root list.
        ind1 = oc[c]+1
        ind2 = oc[c+1]
        #ADDING SPLITTED ELEMENTS TO LIST
        spl.append(values[ind1:ind2])
        #Getting Sum
        mf.dic().var().sUm.append(sum(spl[c]))

        c += 1
###############################################################


###############################################################
str1 = str(spl[0:3])
str2 = c
str3 = ', '.join(map(str, oc[0:5]))
print('''
    We splitted the digital roots by consecutive 9's
    for example, three splitted lists are :- 
    %s
    The total count of 9's is:- %d
    The positions of 9's in digital roots list is:- %s,... etc
'''%(str1, str2, str3))
input("\nPress ENTER to continue\n")
###############################################################

###############################################################
sum_list = mf.dic().var().sUm
for i in range(0, 5):
    print('''
    9 occured at %dth position.
    Sum of values between %dth and %dth position is %d
    '''%(oc[i], oc[i], oc[i+1], sum_list[i]))
###############################################################

###############################################################
print('''
    And so on...

    So we see that the sum is either 43 or 56.


    For more proof, here is the list of all the sums of digital root b/w 9's till 1000 Fibonacci numbers:
    %s
    and so on...
'''%(str(sum_list)))
input("\nPress ENTER to continue\n")
print('''
    So we observed that the digital root of fibonacci numbers have their sums b/w two nines in a pattern and that sums are 43 and 56.
    The python program helped us calculate the sum easily and confirm it over first 1000 different terms!
''')
input("\nPress ENTER to exit\n")
###############################################################