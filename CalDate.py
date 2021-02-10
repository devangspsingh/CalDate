

#CREATED  BY  ~~~~ DEVANG SHAURYA PRATAP SINGH ~~~~
#______________________________________________________________________________________________________________
import Heaven                                   #Heaven is just the file name of my functions
from datetime import date                       #import today's date
today_day=date.today().day
today_month=date.today().month
today_year = date.today().year

Heaven.credits()
#______________________________________________________________________________________________________________


Heaven.instructions()        #used self maded function of instructions

#______________________________________________________________________________________________________________

while True:           #done this to execute this program multiple times


    print()
    print()
#______________________________________________________________________________________________________________

    
    a=(input('Enter Task Number 1 or 2: ---'))            #taking task number     

    Heaven.task_number(a)
    
    
    print()
    print()

#______________________________________________________________________________________________________________     
    

    date=int(input('Enter Date :'))                                  #date 1
    while date>31:
        print ('Don\'t be over smart enter valid date')
        date=int(input('Enter Date :'))

        
    month=int(input('Enter Month:'))                                 #month1
    while month>12:
        print ('Don\'t be over smart enter valid month')
        month=int(input('Enter Month:'))
        
        
    year=int(input('Enter Year :'))                                  #year1


    print()
    print()
#______________________________________________________________________________________________________________     
    

    
    if a=="1":
        
            
        date2=int(input('Enter Date2 :'))                                  #date 2
        while date2>31:
            print ('Don\'t be over smart enter valid date')
            date2=int(input('Enter Date2 :'))
            
        month2=int(input('Enter Month2:'))                                 #month2
        while month2>12:
            print ('Don\'t be over smart enter valid month')
            month2=int(input('Enter Month2:'))

            
            
        year2=int(input('Enter Year2 :'))                                  #year2
            
#______________________________________________________________________________________________________________     
    

    elif a=="2":
        print ('Today\'s date:-',today_day,'/',today_month,'/',today_year)      # putted this command for time period from today
        date2=today_day
        month2=today_month
        year2=today_year

#______________________________________________________________________________________________________________     
    
    (Date1)=str(date)+'/'+str(month)+'/'+str(year)              #GETING DATE 1
    (Date2)=str(date2)+'/'+str(month2)+'/'+str(year2)           #GETING DATE 2

#______________________________________________________________________________________________________________     
    
   #below i have defined the number of days in differnt months

    jan=31


    if year%4==0:   #feb problem1
        feb=29
    else:

        feb=28

    if year2%4==0:  #feb problem2
        feb2=29
    else:
        feb2=28

        
    mar=31
    apr=30
    may=31
    jun=30
    jul=31
    aug=31
    sep=30
    oct=31
    nov=30
    dec=31

#______________________________________________________________________________________________________________     
    

    if month==1:                                #depending upon the number of months it is calculating the number of days in date 1
        dmonth=0
    elif month==2:
        dmonth=jan
    elif month==3:
        dmonth=jan+feb
    elif month==4:
        dmonth=jan+feb+mar
    elif month==5:
        dmonth=jan+feb+mar+apr
    elif month==6:
        dmonth=jan+feb+mar+apr+may
    elif month==7:
        dmonth=jan+feb+mar+apr+may+jun
    elif month==8:
        dmonth=jan+feb+mar+apr+may+jun+jul
    elif month==9:
        dmonth=jan+feb+mar+apr+may+jun+jul+aug
    elif month==10:
        dmonth=jan+feb+mar+apr+may+jun+jul+aug+sep
    elif month==11:
        dmonth=jan+feb+mar+apr+may+jun+jul+aug+sep+oct
    else:
        dmonth=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov



  
    if month2==1:                            #depending upon the number of months it is calculating the number of days in date 2
        dmonth2=0
    elif month2==2:
        dmonth2=jan
    elif month2==3:
        dmonth2=jan+feb2
    elif month2==4:
        dmonth2=jan+feb2+mar
    elif month2==5:
        dmonth2=jan+feb2+mar+apr
    elif month2==6:
        dmonth2=jan+feb2+mar+apr+may
    elif month2==7:
        dmonth2=jan+feb2+mar+apr+may+jun
    elif month2==8:
        dmonth2=jan+feb2+mar+apr+may+jun+jul
    elif month2==9:
        dmonth2=jan+feb2+mar+apr+may+jun+jul+aug
    elif month2==10:
        dmonth2=jan+feb2+mar+apr+may+jun+jul+aug+sep
    elif month2==11:
        dmonth2=jan+feb2+mar+apr+may+jun+jul+aug+sep+oct
    else:
        dmonth2=jan+feb2+mar+apr+may+jun+jul+aug+sep+oct+nov




#______________________________________________________________________________________________________________     
    

    days1=int((year-1)*365.25+dmonth+date)      #have divided by 365.25 because earth revolves sun in 365 and 1/4 days
    days2=int((year2-1)*365.25+dmonth2+date2)
#______________________________________________________________________________________________________________     
    

    if days1>days2:                         #added new variable feb0 which will help later on
        days_bet=days1-days2                #depending upon which date is new it take value of feb either by year1 or year2
        feb0=feb                          
    else:
        days_bet=days2-days1
        feb0=feb2
#______________________________________________________________________________________________________________     
    

    print()
    print()
    print(days_bet,"days are in between date1 and date2")

#______________________________________________________________________________________________________________     
    

    year_bet=int(days_bet//365.25)
    RD=round(days_bet%365.25)

#______________________________________________________________________________________________________________     
    
        
    if RD<=jan:                                    #this whole pyramid is created to calculate number of months efficiently
        RMonth=0                                   #as every month is not of exactly 30 days so I have created this to calculate 
        RDays=RD                                   #correct number of days and months
    elif jan<RD<=(jan+feb0):                                     
        RMonth=1
        RDays=RD-(jan)
    elif jan+feb0<RD<=(jan+feb0+mar):
        RMonth=2
        RDays=RD-(jan+feb0)
    elif jan+feb0+mar<RD<=(jan+feb0+mar+apr):
        RMonth=3
        RDays=RD-(jan+feb0+mar)
    elif jan+feb0+mar+apr<RD<=(jan+feb0+mar+apr+may):
        RMonth=4
        RDays=RD-(jan+feb0+mar+apr)
    elif jan+feb0+mar+apr+may<RD<=(jan+feb0+mar+apr+may+jun):
        RMonth=5
        RDays=RD-(jan+feb0+mar+apr+may)
    elif jan+feb0+mar+apr+may+jun<RD<=(jan+feb0+mar+apr+may+jun+jul):
        RMonth=6
        RDays=RD-(jan+feb0+mar+apr+may+jun)
    elif jan+feb0+mar+apr+may+jun+jul<RD<=(jan+feb0+mar+apr+may+jun+jul+aug):
        RMonth=7
        RDays=RD-(jan+feb0+mar+apr+may+jun+jul)
    elif jan+feb0+mar+apr+may+jun+jul+aug<RD<=(jan+feb0+mar+apr+may+jun+jul+aug+sep):
        RMonth=8
        RDays=RD-(jan+feb0+mar+apr+may+jun+jul+aug)
    elif jan+feb0+mar+apr+may+jun+jul+aug+sep<RD<=(jan+feb0+mar+apr+may+jun+jul+aug+sep+oct):
        RMonth=9
        RDays=RD-(jan+feb0+mar+apr+may+jun+jul+aug+sep)
    elif jan+feb0+mar+apr+may+jun+jul+aug+sep+oct<RD<=(jan+feb0+mar+apr+may+jun+jul+aug+sep+oct+nov):
        RMonth=10
        RDays=RD-(jan+feb0+mar+apr+may+jun+jul+aug+sep+oct)
    elif jan+feb0+mar+apr+may+jun+jul+aug+sep+oct+nov<RD<=(jan+feb0+mar+apr+may+jun+jul+aug+sep+oct+nov+dec):
        RMonth=11
        RDays=RD-(jan+feb0+mar+apr+may+jun+jul+aug+sep+oct+nov)

#______________________________________________________________________________________________________________     
    
    
    print(year_bet,'year(s) ',RMonth,'month(s) ',RDays,'day(s) are between',Date1,'and',Date2 )
    print()
    print()

#______________________________________________________________________________________________________________     
    

    Heaven.end_func()            #used my end function
   
#______________________________________________________________________________________________________________     
    



# I have spend my handful amount of time in making this so you should apprecite it :)

#this code is correctly calulating number days ,years and month  ;keeping in mind the feb month problem


