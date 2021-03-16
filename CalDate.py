from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
import time
import os
import sys
from functools import partial
from datetime import date 

photoimage_list=[]
credits = "created by @devangspsingh"

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'

def Between_Days():

    Month_Name=("January","February","March","April","May","June","July","August","September","October","November","December")
    
    Between_Days=Toplevel()
    image_maker(Between_Days,get_path("CalDateBG.png"))
    windowCreater(Between_Days,'CalDate')
    titleCreator(Between_Days,"Calculate Days between two days")
        
    OptionFrame=Frame(Between_Days,bg="Yellow",border=8,relief=RIDGE)
    OptionFrame.pack(side=TOP,padx=85,pady=20,fill=X)

    Info_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Info_Frame.pack(side=TOP,padx=5,pady=10,fill=X)
    Info_Label=Label(Info_Frame,text=("Enter the dates below:-"),font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Info_Label.pack(side=TOP,padx=5,pady=10,fill=X)

    Data_Entry_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Data_Entry_Frame.pack(side=TOP,padx=5,fill=X)
    Data_Output_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Data_Output_Frame.pack(side=BOTTOM,padx=5,pady=10,fill=X)
   
    year1=IntVar()
    year1_entry=Entry(Data_Entry_Frame,textvariable=year1,font=('calibre',10,'normal'),relief=SUNKEN,width=6)
    year1.set(2021)  
    month1 = StringVar()
    month1_entry=ttk.Combobox(Data_Entry_Frame, textvariable = month1,state="readonly",width=10)
    month1_entry['values']=Month_Name
    month1_entry.current(0)
    date1=IntVar()
    date1_entry=Entry(Data_Entry_Frame,textvariable=date1,font=('calibre',10,'normal'),relief=SUNKEN,width=3)
    date1.set(26)

    year2=IntVar()
    year2_entry=Entry(Data_Entry_Frame,textvariable=year2,font=('calibre',10,'normal'),relief=SUNKEN,width=6)
    year2.set(2021)
    month2 = StringVar()
    month2_entry=ttk.Combobox(Data_Entry_Frame, textvariable = month2,state="readonly",width=10)
    month2_entry['values']=Month_Name
    month2_entry.current(7)
    date2=IntVar()
    date2_entry=Entry(Data_Entry_Frame,textvariable=date2,font=('calibre',10,'normal'),relief=SUNKEN,width=3)
    date2.set(15)

    year1_entry.grid(row=0,column=0,padx=10,pady=10)
    month1_entry.grid(row=0,column=1,padx=10,pady=10)
    date1_entry.grid(row=0,column=2,padx=10,pady=10)
    ButtonMaker2(Data_Entry_Frame,"Today",partial(Set_Today,year1,month1_entry,date1,1,year2,month2_entry,date2),0,4,10,10)

    year2_entry.grid(row=1,column=0,padx=10,pady=10)
    month2_entry.grid(row=1,column=1,padx=10,pady=10)
    date2_entry.grid(row=1,column=2,padx=10,pady=10)
    ButtonMaker2(Data_Entry_Frame,"Today",partial(Set_Today,year1,month1_entry,date1,2,year2,month2_entry,date2),1,4,10,10)

    Data_Output_Text1=StringVar()
    Data_Output_Text2=StringVar()

    def calculation_main_between(name, index, mode):

        year1_value=year1.get()
        month1_value=Month_Name.index(month1.get())+1
        date1_value=date1.get()

        year2_value=year2.get()
        month2_value=Month_Name.index(month2.get())+1
        date2_value=date2.get()

        Tuple_between_feb = (main_calculation_days_inbetween(year1_value,month1_value,date1_value,year2_value,month2_value,date2_value))
        Total_days_in_betweem=Tuple_between_feb[0]
        feb0=Tuple_between_feb[1]

        
        days_to_roundoff=days_to_years_month_days(Total_days_in_betweem,feb0)
        year_bet=days_to_roundoff[0]
        RMonth=days_to_roundoff[1]
        RDays=days_to_roundoff[2]
        
        Data_Output_Text1.set(f"{year_bet}Years {RMonth}months {RDays}days")
        Data_Output_Text2.set(f"{Total_days_in_betweem}Total Days")
            
    Data_Output_Text1.trace("w",calculation_main_between)
    Data_Output_Text2.trace("w",calculation_main_between)
    Data_Output_Text1.set("0 Total Days")
    Data_Output_Text2.set("0 Years 0months 0 Days")

    date1.trace("w",calculation_main_between)
    month1.trace("w",calculation_main_between)
    year1.trace("w",calculation_main_between)

    date2.trace("w",calculation_main_between)
    month2.trace("w",calculation_main_between)
    year2.trace("w",calculation_main_between)

    Data_Output_Label1=Label(Data_Output_Frame,textvariable=Data_Output_Text1,font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Data_Output_Label1.pack(side=BOTTOM,padx=5,pady=10,fill=X)
    Data_Output_Label2=Label(Data_Output_Frame,textvariable=Data_Output_Text2,font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Data_Output_Label2.pack(side=BOTTOM,padx=5,pady=10,fill=X)

def Add_Subtract_Dates():
    Month_Name=("January","February","March","April","May","June","July","August","September","October","November","December")
    
    def Add_Subtract_date(add_or_subtract):
        a = add_or_subtract
        if a=="add":
            add_subtract_var.set("add")
            Data_Output_Text2.set("Additon Mode")
        else:
            add_subtract_var.set("subtract")
            Data_Output_Text2.set("Subtraction Mode")
        Data_Output_Text1.set(Data_Output_Text1.get())
        date1.trace("w",calculation_main_between)
        month1.trace("w",calculation_main_between)
        year1.trace("w",calculation_main_between)
        No_of_days.trace("w",calculation_main_between)
        Data_Output_Text1.trace("w",calculation_main_between)

    Add_Subtract_Dates=Toplevel()
    image_maker(Add_Subtract_Dates,get_path("CalDateBG.png"))
    windowCreater(Add_Subtract_Dates,'CalDate')
    titleCreator(Add_Subtract_Dates,"Add or subtract Dates")

    OptionFrame=Frame(Add_Subtract_Dates,bg="Yellow",border=8,relief=RIDGE)
    OptionFrame.pack(side=TOP,padx=85,pady=20,fill=X)

    Info_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Info_Frame.pack(side=TOP,padx=5,pady=10,fill=X)
    Info_Label=Label(Info_Frame,text=("Enter the dates below:-"),font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Info_Label.pack(side=TOP,padx=5,pady=10,fill=X)

    Data_Entry_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Data_Entry_Frame.pack(side=TOP,padx=5,fill=X)
    Data_Entry_Frame2=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Data_Entry_Frame2.pack(side=TOP,padx=5,fill=X)

    Data_Output_Frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Data_Output_Frame.pack(side=TOP,padx=5,pady=10,fill=X)
    Mode_frame=Frame(OptionFrame,bg="OLIVEDRAB1",border=4,relief=FLAT)
    Mode_frame.pack(side=TOP,padx=5,pady=5,fill=X)

    year1=IntVar()
    year1_entry=Entry(Data_Entry_Frame,textvariable=year1,font=('calibre',10,'normal'),relief=SUNKEN,width=6)
    year1.set(2021)  
    month1 = StringVar()
    month1_entry=ttk.Combobox(Data_Entry_Frame, textvariable = month1,state="readonly",width=10)
    month1_entry['values']=Month_Name
    month1_entry.current(0)
    date1=IntVar()
    date1_entry=Entry(Data_Entry_Frame,textvariable=date1,font=('calibre',10,'normal'),relief=SUNKEN,width=3)
    date1.set(26)
    year1_entry.grid(row=0,column=0,padx=10,pady=10)
    month1_entry.grid(row=0,column=1,padx=10,pady=10)
    date1_entry.grid(row=0,column=2,padx=10,pady=10)
    ButtonMaker2(Data_Entry_Frame,"Today",partial(Set_Today,year1,month1_entry,date1),0,4,10,10)

    No_of_days=IntVar()
    No_of_days_entry=Entry(Data_Entry_Frame2,textvariable=No_of_days,font=('calibre',10,'normal'),width=14,relief=SUNKEN)
    No_of_days.set("number of days")
    No_of_days_entry.pack(padx=10,pady=10,side=LEFT)
    Data_Output_Text2=StringVar()
    Data_Output_Text2.set("Additon Mode")
    ButtonMaker3(Data_Entry_Frame2,"Add",partial(Add_Subtract_date,"add"),)
    ButtonMaker3(Data_Entry_Frame2,"Subtract",partial(Add_Subtract_date,"subtract"))

    add_subtract_var=StringVar()
    Data_Output_Text1=StringVar()

    def calculation_main_between(name, index, mode):

        year1_value=year1.get()
        month1_value=Month_Name.index(month1.get())+1
        date1_value=date1.get()
        no_of_days_value=No_of_days.get()
        
        days_in_new_date=days_in_new_date_finder(year1_value,month1_value,date1_value,no_of_days_value,add_subtract_var.get())[0]
        feb=days_in_new_date_finder(year1_value,month1_value,date1_value,no_of_days_value)[1]
        new_date_tuple=days_to_new_date(days_in_new_date,feb,year1_value)
        new_year=new_date_tuple[0]
        new_month=new_date_tuple[1]
        new_date=new_date_tuple[2]

        # print(f"{new_year}/{new_month}/{new_date}")
        
        Data_Output_Text1.set(f" {new_year} {Month_Name[new_month-1]} {new_date} ")

    Data_Output_Text1.trace("w",calculation_main_between)
    Data_Output_Text1.set(f" {year1.get()} {Month_Name[Month_Name.index(month1.get())+1-1]} {date1.get()} ")

    date1.trace("w",calculation_main_between)
    month1.trace("w",calculation_main_between)
    year1.trace("w",calculation_main_between)
    No_of_days.trace("w",calculation_main_between)

    Data_Output_Label1=Label(Mode_frame,textvariable=Data_Output_Text2,font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Data_Output_Label1.pack(side=BOTTOM,padx=5,pady=10,fill=X)

    Data_Output_Label2=Label(Data_Output_Frame,textvariable=Data_Output_Text1,font="compact 10 bold",padx=5,fg="blue",bg="OLIVEDRAB1")
    Data_Output_Label2.pack(side=BOTTOM,padx=5,pady=10,fill=X)

def windowCreater(root,title_name):
    bgcolor="green2"
    fgcolor="white"
    h=500
    w=500
    postionx=40
    postiony=40
    root.geometry(f"{h}x{w}+{postionx}+{postiony}")
    root.maxsize(h,w)
    root.minsize(h,w)

    root.title(title_name)
    root.iconbitmap(get_path("CalDateIcon.ico"))
    
    status_frame=Frame(root,bg=bgcolor,border=5,relief=FLAT)
    status_bar=Label(status_frame,bg=bgcolor,fg=fgcolor,justify=LEFT,anchor=W)
    status_frame.pack(side=BOTTOM,fill=X)
    status_bar.pack(side=LEFT)
    Label(status_frame,text=credits,bg=bgcolor,fg=fgcolor,font="times 10",justify="right",anchor=E,).pack(side=RIGHT)
    def clock():
        time_string=time.strftime('%I:%M:%S:%p',time.localtime())
        if time_string!='':
            status_bar.config(text=time_string,font='times 10',padx=10)
        root.after(100,clock)
    clock()

def image_maker(window,name):
    background_image=Image.open(name)
    background_image=background_image.resize((500,500),Image.ANTIALIAS)
    background_image=ImageTk.PhotoImage(background_image)
    photoimage_list.append(background_image)
    background_image_label=Label(window,image=background_image)
    background_image_label.place(x=0,y=0)

def titleCreator(window,text):
    bgcolor="green2"
    fgcolor="white"
    TitleFrame=Frame(window,bg=bgcolor,border=5,relief=RIDGE)
    TitleLabel=Label(TitleFrame,text=text,font="compact 20 bold",padx=5,fg=fgcolor,bg=bgcolor)
    TitleFrame.pack(side=TOP,fill=X,padx=15,pady=8)
    TitleLabel.pack(side=TOP,pady=15)

def ButtonMaker(ButtonFrame,Text,Command):
    bgcolor="OLIVEDRAB1"
    Button(ButtonFrame,anchor="w",pady=-2,padx=2,text=Text,font="compact 12 ",command=Command,bg=bgcolor,fg="Black",activebackground="orange").pack(expand=YES,padx=6,pady=5,fill=X,anchor=W)

def ButtonMaker2(ButtonFrame,Text,Command,r,c,y,x):
    bgcolor="sienna1"
    Button(ButtonFrame,fg="white",anchor="w",pady=0,padx=8,text=Text,font="compact 8 bold",command=Command,bg=bgcolor,activebackground="orange").grid(row=r,column=c,pady=y,padx=x)   

def ButtonMaker3(ButtonFrame,Text,Command):
    bgcolor="sienna1"
    Button(ButtonFrame,fg="white",pady=0,padx=1,text=Text,font="compact 9 bold",command=Command,bg=bgcolor,width=8,activebackground="orange").pack(side=LEFT,padx=10,pady=10)   

def main_calculation_days_inbetween(year1_value=2020,month1_value=1,date1_value=10,year2_value=2020,month2_value=2,date2_value=20):
    #give provide 2 dates in yy mm dd - yy mm dd it will return days in between
    if year1_value%4==0:   #feb problem1
        feb=29
    else:
        feb=28
    if year2_value%4==0:  #feb problem2
        feb2=29
    else:
        feb2=28
    jan=31    
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
    if month1_value==1:                                #depending upon the number of months it is calculating the number of days in date 1
        days_in_month1_value=0
    elif month1_value==2:
        days_in_month1_value=jan
    elif month1_value==3:
        days_in_month1_value=jan+feb
    elif month1_value==4:
        days_in_month1_value=jan+feb+mar
    elif month1_value==5:
        days_in_month1_value=jan+feb+mar+apr
    elif month1_value==6:
        days_in_month1_value=jan+feb+mar+apr+may
    elif month1_value==7:
        days_in_month1_value=jan+feb+mar+apr+may+jun
    elif month1_value==8:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul
    elif month1_value==9:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug
    elif month1_value==10:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep
    elif month1_value==11:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep+oct
    else:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov

    if month2_value==1:                            #depending upon the number of months it is calculating the number of days in date 2
        days_month2_value=0
    elif month2_value==2:
        days_month2_value=jan
    elif month2_value==3:
        days_month2_value=jan+feb2
    elif month2_value==4:                               
        days_month2_value=jan+feb2+mar
    elif month2_value==5:
        days_month2_value=jan+feb2+mar+apr
    elif month2_value==6:
        days_month2_value=jan+feb2+mar+apr+may
    elif month2_value==7:
        days_month2_value=jan+feb2+mar+apr+may+jun
    elif month2_value==8:
        days_month2_value=jan+feb2+mar+apr+may+jun+jul
    elif month2_value==9:
        days_month2_value=jan+feb2+mar+apr+may+jun+jul+aug
    elif month2_value==10:
        days_month2_value=jan+feb2+mar+apr+may+jun+jul+aug+sep
    elif month2_value==11:
        days_month2_value=jan+feb2+mar+apr+may+jun+jul+aug+sep+oct
    else:
        days_month2_value=jan+feb2+mar+apr+may+jun+jul+aug+sep+oct+nov

    days1=int((year1_value-1)*365.25+days_in_month1_value+date1_value)      #have divided by 365.25 because earth revolves sun in 365 and 1/4 days
    days2=int((year2_value-1)*365.25+days_month2_value+date2_value)

    if days1>days2:                         #added new variable feb0 which will help later on
        days_bet=days1-days2                #depending upon which date is new it take value of feb either by year1 or year2
        feb0=feb                          
    else:
        days_bet=days2-days1
        feb0=feb2
    
    return (days_bet,feb0)

    # print(days_bet,"days are in between date1 and date2")

def days_to_years_month_days(days_bet,feb0):
    #provide number of days in betwween 2 days , and the number of days in month feb of latest date

    jan=31    
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
    year_bet=int(days_bet//365.25)
    RD=round(days_bet%365.25)
    
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

    return(year_bet,RMonth,RDays)
    # print(year_bet,'year(s) ',RMonth,'month(s) ',RDays,'day(s) are between')

def Set_Today(year1,month1_entry,date1,a=1,year2=0,month2_entry=0,date2=0):
    today_date=date.today().day
    today_month=date.today().month
    today_year = date.today().year

    if a == 1:
        date1.set(today_date)
        month1_entry.current(today_month-1)
        year1.set(today_year)
    else :
        date2.set(today_date)
        month2_entry.current(today_month-1)
        year2.set(today_year) 

def days_in_new_date_finder(year1_value=2020,month1_value=1,date1_value=10,no_of_days_value=0,add_subtract="add"):
    #give provide 2 dates in yy mm dd - yy mm dd it will return days in between

    if year1_value %4==0:  
        feb=29
    else:
        feb=28
    jan=31    
    mar=31
    apr=30
    may=31
    jun=30
    jul=31
    aug=31
    sep=30
    oct=31
    nov=30

    if month1_value==1:                                #depending upon the number of months it is calculating the number of days in date 1
        days_in_month1_value=0
    elif month1_value==2:
        days_in_month1_value=jan
    elif month1_value==3:
        days_in_month1_value=jan+feb
    elif month1_value==4:
        days_in_month1_value=jan+feb+mar
    elif month1_value==5:
        days_in_month1_value=jan+feb+mar+apr
    elif month1_value==6:
        days_in_month1_value=jan+feb+mar+apr+may
    elif month1_value==7:
        days_in_month1_value=jan+feb+mar+apr+may+jun
    elif month1_value==8:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul
    elif month1_value==9:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug
    elif month1_value==10:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep
    elif month1_value==11:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep+oct
    else:
        days_in_month1_value=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov

    
    days1=int((year1_value-1)*365.25+days_in_month1_value+date1_value)      #have divided by 365.25 because earth revolves sun in 365 and 1/4 days
    
    if add_subtract=="add":
        days_in_new_date=(days1+no_of_days_value)
    if add_subtract=="subtract":
        days_in_new_date=(days1-no_of_days_value)
    
    return (days_in_new_date,feb)

def days_to_new_date(days_bet,feb0,year1_value):
    #provide number of days in betwween 2 days , and the number of days in month feb of latest date
    
    jan=31    
    mar=31
    apr=30
    may=31
    jun=30
    jul=31
    aug=31
    sep=30
    oct=31
    nov=30

    year_bet=int(days_bet//365.25)
    RD=round(days_bet%365.25)
    
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

    if year1_value%4==0:
        return(year_bet+1,RMonth+1,RDays+1)

    else:
        return(year_bet+1,RMonth+1,RDays)
    # print(year_bet,'year(s) ',RMonth,'month(s) ',RDays,'day(s) are between')

if __name__ == "__main__":      
    root=Tk()

    image_maker(root,get_path("CalDateBG.png"))
    windowCreater(root,'CalDate')
    titleCreator(root,"Date Calculator")

    OptionFrame=Frame(root,bg="Yellow",border=8,relief=RIDGE)
    OptionLabel=Label(OptionFrame,text="Select from below:-",font="compact 13 bold",padx=5,fg="blue",bg="yellow")
    OptionFrame.pack(side=TOP,padx=80,pady=50,ipady=40,fill=X)
    OptionLabel.pack(side=TOP,ipady=10,padx=15,pady=5)

    ButtonMaker(OptionFrame,"1.Calculate Days between two days",Between_Days)
    ButtonMaker(OptionFrame,"2.Add or subtract Dates",Add_Subtract_Dates)

    Label(OptionFrame,text="______________",font="compact 13 bold",padx=5,fg="blue",bg="yellow").pack(side=BOTTOM,ipady=10,padx=15,pady=5)

    root.mainloop()