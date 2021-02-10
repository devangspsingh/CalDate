def line2():
    print()
    print()
#______________________________________________________________________________________

def end_func():              #defined a function which will enhance user experience
    print()
    print()
    a=input("Press X to end program  or any other key to run again:-->")        
    end=a.upper()              # this is changing the input of varible {a} to upper case#                                                 
    if end=="X":    
        exit()                 #this is exit command; this ends our program 
    else :
        print()
        print("       ","-"*35)
        print()
 


#______________________________________________________________________________________


def instructions():
    print('''

Hello!!!!   :)



Some instructions regarding this program :-

  You will be asked to \"enter Date\" in that column you have to put date in number means if date is 23 August 2008,
  Then values will be, Date : 23
                       Month: 8 or 08
                       Year : 2008



    Select Task Number

    1.You can calculate number of days or years,months,days between two days.
    2.Calculate number of days,months,years between Today and any other date.


  --------By the way thanks for using it --------
  
  ''')

#----------------------------------------------------------------------------------------------

def task_number(a):
    if a=='1':
        
        print()
        print()
        print('Calculate time period between two different dates')
        
    elif a=='2':
        
        print()
        print()
        print('Calculate time period between today and other date')                      

    while a!= '1' and a!= '2' :                            #created to get rid of problem of wrong inputs
        print() 
        print('Enter valid task number.')
        print()
        a=(input('Enter Task Number 1 or 2: ---'))
        if a=='1':
        
            print()
            print()
            print('Calculate time period between two different dates')
            break
            
        elif a=='2':
            
            print()
            print()
            print('Calculate time period between today and other date')
            break

    return a


#-----------------------------------------------------------------------------------------------------



def credits():
    print('''created by @DevangShauryaPratapSingh
Class - 11 (PCM)

Thanks for using it :)''')

def ThankSIR():
    print('''SPECIAL THANKS TO ARPAN GUPTA SIR''')
    
#-----------------------------------------------------------------
    
