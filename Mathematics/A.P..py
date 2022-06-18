#h is the first term of A.P.
a=int(input("Enter the first term of A.P.: "))
d=int(input("Enter the common difference of A.P.: "))
er = input('If you do not know the last term, then type "yes" and it will go for the first ten terms of the AP , otherwise continueby ignoring this: ')

if er=='yes':
    l=a+9*d
    if (a>0) and (d>0) and (l>0):#it runs!
        
        while a <=l:#last term
            
            print(a)
            a+=d #common difference addition

    if (a<0) and (d>0) and (l>0):#it runs!
        while a <= l :
            print(a)
            a+=d

    if (a>0)and (d<0)and (l>0):#it runs!
        while a >= l:
            print(a)
            a+=d
    input('Press ENTER to exit')

else:
       l=int(input("Enter the (term just after)last term of A.P.: "))

       if (a<0)and (d<0)and (l<0):#it runs!
        while a >= l:
               print(a)
               a+=d

       if (a<0)and (d>0)and (l<0):#it runs!
        while a <= l:
               print(a)
               a+=d
        
       if (a>0) and (d>0) and (l>0):#it runs!
        while a <=l:#last term
               print(a)
               a+=d #common difference addition

       if (a<0) and (d>0) and (l>0):#it runs!
        while a <= l :
               print(a)
               a+=d

       if (a>0)and (d<0)and (l>0):#it runs!
        while a >= l:
               print(a)
               a+=d

       if (a<0)and (d<0)and (l<0):#it runs!
        while a >= l:
               print(a)
               a+=d

       if (a<0)and (d>0)and (l<0):#it runs!
        while a <= l:
               print(a)
               a+=d
        
       input('press ENTER to exit')
