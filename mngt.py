from Car import car
import datetime
import random
from prettytable import PrettyTable
from tabulate import tabulate
from colorama import init, Fore
init()
class managemnet:
    def add(self,c):
        with open("cars.txt",'a') as fp:
                    fp.write(str(c)) 
                    print("\t\t\t\t New Car Added Succesfully")
         

    def display(self):
        table=[]
        header=["Car Name", "Reg. No", "Rent/day", "Avail", "Numbers", "Rented"]
        with open('cars.txt','r') as fp:
            print("\033[1m**************** WELCOME TO ZOOM RENTAL CARS ********************\033[0m\n")
            for x in fp:
                car_info = x.strip().split(' || ')
                table.append(car_info)
            print(tabulate(table, headers=header, tablefmt="simple"))
            print("\n\033[1m**************** WELCOME TO ZOOM RENTAL CARS ********************\033[0m\n")

    
    def search(self,name):
        table=[]
        header=[" CAR NAME","REG.No","RENT/DAY","AVILABLITY","RENTED"]
        with open('cars.txt','r') as fp:
            for cars in fp:
                split=cars.split(" || ")
                if (split[0]==str(name)):
                    table.append(split)
                    print(tabulate(table, headers=header, tablefmt="pipe"))
                    # print('\n Car Found:',cars)
                    break
            else:
                print("Not found")
                
    def delete (self,name):
        filter_data=''
        with open('cars.txt','r') as fp:
            data=fp.readlines()
            filter_data=[d for d in data if name not in d  ]
            print("CAR Deleted")
        with open('cars.txt','w') as f:
            f.writelines(filter_data)
            print("DATA UPDATED AFTER DELETE CAR")
    
    def update(self):
        try:
            name=input("ENTER CAR NAME TO UPADTE:").upper()
            if not all(char.isdigit or char.isalpha() or char.isspace() for char in name):
                raise ValueError("CAR NAME SHOULD CONTAIN ONLY ALPHABETIC CHARACTER")
            data=[]
            isfound=False
            with open('cars.txt','r') as fp:
                for ele in fp:
                    split=ele.split(' || ')
                    if (split[0]==str(name)):
                        isfound=True
                        print("""
                            1.Name 
                            2.Rent
                            """)
                        ch=int(input("Enter your Choice:"))
                        if ch==1:
                            new_name=input("Enter New Name:").upper()
                            split[0]=new_name
                            ele=' || '.join(split)
                            data.append(ele)
                        elif ch==2:
                            new_rent=str(int(input("Enter New Rent :")))
                            if new_rent<0:
                                raise ValueError("RENT PRICE SHOULD NOT LESS THAN 500 RS ")
                            split[2]=new_rent
                            ele=' || '.join(split)
                            data.append(ele)
                    else:
                        data.append(ele)
            if isfound==True:
                with open('cars.txt','w') as fp:
                    for x in data:
                        fp.write(x)
            else:
                print("Record Not Found")
        except ValueError as v:
            print(v)
    
    def rent_car(self,name,id,car_name,Deposit):
        car_rand_id=random.randint(0,1000)
        # car_id=str(int(input("Enter Car Id:"))
        list=[]
        found=False
        with open('cars.txt','r') as fp:
            for i in fp:
                splited_text=i.split(' || ')
                if (str(car_name) in str(splited_text[0])) and (str(splited_text[3])>str(0)):
                    found=True
                    splited_text[3]=str(int(splited_text[3])-1)
                    splited_text[4]=str(int(splited_text[5])+1)
                    i=" || ".join(splited_text)+'\n'
                    list.append(i)
                    
                    
                    rent_date=input("\033[1m ENTER DATE(DD-MM-YYYY) 📅:\033[0m") #User date
                    date_1=datetime.datetime.strptime(rent_date,"%d-%m-%Y")
                    date_2=date_1.date()
                    date_3=date_2.strftime('%d-%m-%Y')
                                    

                    with open ("Rented.txt",'a') as f:
                        f.write(f"{car_rand_id} || {name} || {id} || {car_name} || {date_3} || NA || 0 || {Deposit}"+'\n')
                        print(f"\n\n CAR RENTED SUCCESSFULLY ✅")  
                else:
                    list.append(i)
        if found==True:
          with open('car.txt','w') as fp:
              for x in list:
                  fp.write(x)
                  
        else:
            print("Car Not Found Enter valid car Name") 
            
    def return_car(self,name):
        list=''
        table=[]
        header=["Car ID", " NAME", " AADHAR NO ", " CAR NAME"," RENTED DATE","RETURN DATE","TOTAL BILL","DEPOSIT AMOUNT"]
        with open ('Rented.txt','r') as fp:
            for i in fp:
                split_text=i.strip().split(' || ')
                if name in split_text:
                    table.append(split_text)
                    print(tabulate(table, headers=header, tablefmt="grid"))
                    break
            else:
                print("USER NOT FOUND")
                            
        found=False
        with open('Rented.txt','r') as f:
            ask=input("\n\n ENTER WHICH CAR YOU WANT TO RETURN ENTER CAR ID:")
            for i in f:
                splited_text=i.split(' || ')
                if ask in splited_text:
                    # print("FOUND")
                    list=i
                    data=list.split(' || ')
                    data[5]=datetime.datetime.today().strftime('%d-%m-%Y')
                    # print(data)
                    found=True
                    return_date=datetime.date.today()
                    date_diff =(return_date-datetime.datetime.strptime(data[4],'%d-%m-%Y').date()).days
                    
                    # print(date_diff)
                    break
            else:
                print("WROND ID YOU ENTERD")
        
        
        if found==True:
            cars=[]
            with open('cars.txt','r') as file:
                for i in file:
                    split=i.split(' || ')
                    if split[0]==data[3]:
                       Bill_amt = int(split[2]) * date_diff
                       final_bill=Bill_amt+(Bill_amt*0.18)
                       print("\n\n YOUR TOTAL BILL INCLUDING 18% GST 💵 :",final_bill)
                       if final_bill<0:
                           print("ERROR OCCURED IN YOUR DATE PLEASE CHECK YOUR DATE")
                       
                       deposit_amt=final_bill-int(data[7])
                       if deposit_amt<0:
                            rem=deposit_amt*(-1)
                            print("\n\n PLEASE TAKE REMAINING BALANCE FROM DEPOSIT 💵 :",rem)
                        
                       else:
                            print("\n\n PLEASE PAY REMAINING AMOUNT AFTER DEDUCTION FROM DEPOSIT 💵 :",deposit_amt)
                        #    print("\n\n PLEASE TAKE YOUR DEPOSIT AMOUNT 💵 :",data[7])
                            print("\n\n CAR RETURNED ✅ ")
                       split[3]=str(int(split[3])+1)
                       split[4]=str(int(split[4])-1)
                       i=" || ".join(split)+'\n'
                       cars.append(i)
                       with open ('Return.txt','a',encoding='utf-8') as fp:
                        fp.write(f"{data[0]} || {data[1]} || {data[2]} || {data[3]} || {data[4]} || {data[5]} || {final_bill} ₹ || {data[7]}"+'\n')
                        # print("DATA INSERTED")
                        
                        filter_data=''
                        with open('Rented.txt','r') as fp:
                            read=fp.readlines()
                            filter_data=[d for d in read if ask not in d  ]
                        with open('Rented.txt','w') as f:
                            f.writelines(filter_data)
                            # print("DATA UPDATED")
                    
                    else:
                        cars.append(i)
            with open('car.txt','w') as fp:
              for x in cars:
                  fp.write(x)
                  
    def rented_display(self):
        table=[]
        header=["Car ID", " NAME", " AADHAR NO "," CAR NAME"," RENTED DATE","RETURN DATE","TOTAL BILL","DEPOSITED AMT"]
        with open ("Rented.txt",'r')as f:
            print("\033[1m****************************************** RENTED RECORDS ****************************************************\033[0m\n")
            # print('{:<15}{:<10}         {:<10}          {:<10}         {:<10}       {:<10}     {:<10}'.format("Car ID", " NAME", " PROOF", " CAR NAME"," RENTED DATE","RETURN DATE","TOTAL BILL"+'\n'))
            for i in f:
                split_text=i.strip().split(' || ')
                table.append(split_text)
            print(tabulate(table, headers=header, tablefmt="pipe"))
            
                # if len(split) >= 7:  # Assuming there are at least 7 elements
                    # print('{:<15}{:<10}       {:<10}         {:<10}        {:<10}          {:<10}        {:<10} '.format(*split)+'\n')      
            print("\n\033[1m****************************************** RENTED RECORDS ****************************************************\033[0m")
                                  
    def return_display(self):
        table=[]
        header=["Car ID", " NAME", " AADHAR NO", " CAR NAME"," RENTED DATE","RETURN DATE","TOTAL BILL","DEPOSIT AMT"]
        with open ("Return.txt",'r',encoding='utf-8')as f:
            print("\033[1m******************************************RETURN CAR RECORDS*****************************************************\033[0m\n\n")
           
            # print('\t\t\t'+'{:<15}{:<10}         {:<10}          {:<10}         {:<10}       {:<10}     {:<10}'.format("Car ID", " NAME", " PROOF", " CAR NAME"," RENTED DATE","RETURN DATE","TOTAL BILL"+'\n'))
            for i in f:
                split=i.split(' || ')
                table.append(split)
            print(tabulate(table, headers=header, tablefmt="pipe"))
                    # print('\t\t\t'+'{:<15}{:<10}       {:<10}         {:<10}        {:<10}          {:<10}        {:<10} '.format(*split)+'\n') 
            print("\n\n\033[1m******************************************RETURN  CAR RECORDS*****************************************************\033[0m")                    
                       
                                                
                        
           
                
                    

                    
                    

                    
           
            
            
                
        
        
        
        
                                  

                            
        
        