from user import user
from Car import car
from mngt import managemnet
from error import *
import random
if (__name__=="__main__"):
    obj=managemnet()
    role=input("Enter Your Role Admin(A) or User(U):")
    if role.capitalize()=="A":
        password=1212
        admin=int(input("Enter Password:"))
        if password==admin:
            
            Choice=0
            while Choice!=10:
                print("""
                    \t\t\t\t*************************\t\t\t\t
                    \t\t\t\t* 1.Add Cars            *\t\t\t\t
                    \t\t\t\t* 2.Display Cars        *\t\t\t\t
                    \t\t\t\t* 3.Search Cars         *\t\t\t\t
                    \t\t\t\t* 4.Delete Cars         *\t\t\t\t
                    \t\t\t\t* 5.Update Cars         *\t\t\t\t
                    \t\t\t\t* 6.Rent Car            *\t\t\t\t
                    \t\t\t\t* 7.Return Car          *\t\t\t\t
                    \t\t\t\t* 8.Display Rented Cars *\t\t\t\t
                    \t\t\t\t* 9.Display Return Cars *\t\t\t\t
                    \t\t\t\t* 10.Exit               *\t\t\t\t
                    \t\t\t\t*************************\t\t\t\t
                    """)
                Choice=int(input("Enter Choice:"))
                if (Choice==1):
                    name=input("\t\t\t\t Enter Car Name: ")
                    reg_no=input("\t\t\t\t Enter Reg No: ")
                    price=int(input("\t\t\t\t Enter Rent: "))
                    avail=int(input("\t\t\t\t Enter available Cars:"))
                    with open("car.txt",'r') as fp:
                        for i in fp:
                            split=i.split(' || ')
                            if name in split[0]:
                                print("Car is already Exist")
                                break
                        else:    
                            c=car(name,reg_no,price,avail)
                            obj.add(c)

                elif (Choice==2):
                    obj.display()
                    
                elif(Choice==3):
                    id=input("\t\t\t\tEnter Car Name:")
                    print()
                    obj.search(id)
                
                elif(Choice==4):
                    name=input("\t\t\t\tEnter Car Name:") 
                    print()   
                    obj.delete(name)
                    
                elif(Choice==5):
                    obj.display()
                
                    obj.update()
                    
                elif (Choice==6):
                
                    obj.display()
                    name=input("\t\t\t\t Enter Your Name:")
                    id=int(input("\t\t\t\t Enter PAN  Proof:"))
                    if len(str(id))<12 or len(str(id))>12:
                        print("Enter Valid Proof Id")

                    else:                   
                        car_name=input("\t\t\t\t Enter Car Name:")
                        U=user(name,id,car_name)
                        obj.rent_car(name,id,car_name)
                
                        
                elif (Choice==7):
                    u_name=input("\t\t\t\t Enter Your Name:")
                    obj.return_car(u_name)
                
                elif (Choice==8):
                    obj.rented_display()
                    
                elif (Choice==9):
                    obj.return_display()
        else:
            print("WRONG PASSWORD")
    elif role.capitalize()=="U":
        u_choice=0
        while u_choice!=5:
            print("""
                  1.DISPLAY CARS
                  2.SEARCH CARS
                  3.RENT CAR
                  4.RETURN CAR
                  5.EXIT
                  """)
            u_choice=int(input("ENTER YOUR CHOICE:"))
            if u_choice==1:
                obj.display()
            elif u_choice==2:
                find=input("ENTER CAR NAME:")
                obj.search(find)
            elif u_choice==3:
                name=input("\t\t\t\t Enter Your Name:")
                id=int(input("\t\t\t\t Enter PAN  Proof:"))
                if len(str(id))<12 or len(str(id))>12:
                    print("Enter Valid Proof Id")

                else:                   
                    car_name=input("\t\t\t\t Enter Car Name:")
                    U=user(name,id,car_name)
                    obj.rent_car(name,id,car_name)
            elif u_choice==4:
                u_name=input("\t\t\t\t Enter Your Name:")
                obj.return_car(u_name)
            else:
                print("EXITED")
                
            
            
        
        
            
            
            
