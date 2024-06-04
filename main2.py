from user import user
from Car import car
from mngt import managemnet
from colorama import init, Fore
import random as rd
init()
if (__name__=="__main__"):
    obj=managemnet()
    
    print(Fore.LIGHTYELLOW_EX,"\n\n\t\t\t\t\033[1m|=|=|=|=|=|=|=|=|=|=|=* 🟢🚗🚘 WELCOME TO ZOOM RENTAL CARS 🚘🚗🟢 *=|=|=|=|=|=|=|=|=|=|=|\n\n\033[0m"+Fore.RESET)

    while True:    
        role=input("\033[1m Enter Your Role Admin(A) 👨‍💻 or User(U) 🧑 👩:\033[0m")

        if role.capitalize()=="A":
            try:
                password=1212
                admin=int(input("\033[1m Enter Password 🔑 :\033[0m"))
                if password!=admin:
                    raise ValueError("PLEASE ENTER VALID PASSWORD")
                if password==admin:
                    Choice=0
                    while Choice!=8:
                        print(Fore.LIGHTMAGENTA_EX+"""\n\n\t\t\t\t\t\t\033[1m=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n
                        \t\t\t\t\t\t MAIN MENU 🗃 \n\n
                        \t\t\t\t* 1️⃣ .Add Cars     🚘             6️⃣ .Display Rented Cars 📖🚘        
                        \t\t\t\t* 2️⃣ .Display Cars 👀             7️⃣ .Display Return Cars 📖🔄🚘      
                        \t\t\t\t* 3️⃣ .Search Cars  🔎             8️⃣ .Exit                ❌           
                        \t\t\t\t* 4️⃣ .Delete Cars   🗑                                                   
                        \t\t\t\t* 5️⃣ .Update Cars  📝                                         
                        \t\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\033[0m\t\t\t\t
                        """)
                        Choice=int(input("Enter Choice:"))
                        if (Choice==1):
                            try:
                                name=input("\033[1m Enter Car Name: \033[0m").upper()
                                if not all(char.isdigit() or char.isalpha() or char.isspace() for char in name):
                                    raise ValueError("Name  should contain only alphabetic characters and spaces.")
                                reg_no=input("\033[1m Enter Reg No: \033[0m").upper()
                                if len(reg_no)>10 or len(reg_no)<10:
                                    raise ValueError("REGISTRATION NUMBER IS NOT VALID")
                                price=int(input("\033[1m Enter Rent: \033[0m"))
                                if price<500:
                                    raise ValueError("CAR RENT PRICE SHOULD NOT LESS THAN 500")
                                avail=int(input("\033[1m Enter available Cars:\033[0m"))
                                if avail<0:
                                    raise ValueError("AVAILABLE CAR ENTRY SHOULD NOT LESS THAN 0 ")
                                # num = ["MH13" +"HR"+ str(rd.randint(1000, 9999)) for i in range(1, avail + 1)]
                                num = [ str(rd.randint(1000, 9999)) for i in range(1, avail + 1)]    
                                    
                                # with open("cars.txt",'r') as f:
                                #     for i in fp:
                                #         split=i.split(' || ')
                                #         if str(c) in split[0]:
                                #             print("Car is already Exist")
                                #             break
                                #     else: 
                                c=car(name,reg_no,price,avail,num)
                                obj.add(c)
                            except ValueError as v:
                                print(v)

                        elif (Choice==2):
                            obj.display()
                            
                        elif(Choice==3):
                            try:
                                name_car=input("\033[1m Enter Car Name:\033[0m").upper()
                                if not all(char.isdigit or char.isalpha() or char.isspace() for char in name_car):
                                    raise ValueError("Name  should contain only alphabetic characters and spaces.")
                                obj.search(name_car)
                            except TypeError as v:
                                print(v)
                        
                        elif(Choice==4):
                            try:
                                name=input("\033[1m Which car you want to delete enter car name : \033[0m").upper() 
                                if not all(char.isdigit() or char.isalpha() or char.isspace() for char in name):
                                    raise ValueError("Name should contain only alphabetic characters and spaces.")
                                obj.delete(name)
                            except TypeError as v:
                                print(v)
                            
                        elif(Choice==5):
                            obj.display()
                        
                            obj.update()
                        
                        elif (Choice==6):
                            obj.rented_display()
                            
                        elif (Choice==7):
                            obj.return_display()
                # else:
                #     print("WRONG PASSWORD")
            except ValueError as v:
                print(v)
        elif role.capitalize()=="U":
            print("""\033[1m
                1️⃣ .Register ✒
                2️⃣ .Login 🔐
                3️⃣ .Exit to Main Menu ❌
                \033[0m""")
            ch=int(input("\033[1m Enter Your Choice:\033[0m"))
            if ch==1:
                try:
                    username=input("\033[1m Enter Your Username:\033[0m").lower()
                    if not all(char.isalpha() or char.isspace() for char in username):
                        raise ValueError("Username should contain only alphabetic characters and spaces.")
                    Create_pass=input("\033[1m Enter Password:\033[0m").lower()
                    with open("user.txt",'r') as f:
                        for i in f:
                            split=i.split(' || ')
                            if split[0]==username and split[1]==Create_pass:
                                print("USERNAME AND PASSWROD ALREADY EXIST")
                                break
                        else:
                            with open("user.txt",'a') as fp:
                                fp.write(f"{username} || {Create_pass} || User"+'\n')
                                print("REGISTERD SUCCESSFULLY")
                except ValueError as v:
                    print(v)

            elif ch==2:
                username=input("\033[1m Enter Your Username 🪧: \033[0m").lower()
                pwd=input("\033[1m Enter Password 🔑:\033[0m").lower()
                with open("user.txt",'r') as fp:
                    for i in fp:
                        splited_text=i.strip().split(" || ")
                        if splited_text[0]==username and splited_text[1]==pwd and splited_text[2]=='User':
                            u_choice=0
                            while u_choice!=5:
                                print(Fore.LIGHTGREEN_EX+"""\033[1m
                                \t\t\t\t    MENU 🗄 \n\n
                                \t\t\t\t    1️⃣ .DISPLAY CARS  👀
                                \t\t\t\t    2️⃣ .SEARCH CARS   🔎
                                \t\t\t\t    3️⃣ .RENT CAR      🛒🚘
                                \t\t\t\t    4️⃣ .RETURN CAR    🔄🚘
                                \t\t\t\t    5️⃣ .EXIT          ❌
                                    \033[0m""")
                                u_choice=int(input("\033[1m ENTER YOUR CHOICE: \033[0m"))
                                if u_choice==1:
                                    obj.display()
                                elif u_choice==2:
                                    try:
                                        find=input("\033[1m Enter Car Name:\033[0m").upper()
                                        if not all(char.isdigit() or char.isalpha() or char.isspace() for char in find):
                                            raise ValueError("Name should contain only alphabetic characters and spaces.")
                                        obj.search(find)
                                    except ValueError as v:
                                        print(v)
                                elif u_choice==3:
                                    try:
                                        name=input("\033[1m Enter Your Name 🪧 :\033[0m").upper()
                                        if not all( char.isalpha() or char.isspace() for char in name):
                                            raise ValueError("NAME SHOULD CONTAIN ONLY ALPHABETIC CHARACTER")
                                        
                                        deposit=int(input("\033[1m ENTER DEPOSIT AMOUNT 💵 :\033[0m"))
                                        if deposit<1000:
                                            raise ValueError("DEPOSIT AMOUNT SHOULD BE GREATER THAN 1000")
                                    
                                        id=int(input(" \033[1m Enter Aadhar Details 💳 : \033[0m"))
                                        if len(str(id))<12 or len(str(id))>12:
                                            print("\033[1m Enter Valid 12 digit Aadhar Detail \033[0m")
                                            
                                        else:
                                            car_name=input("\033[1m Enter Car Name 🚘 :\033[0m").upper()
                                            U=user(name,id,car_name)
                                            obj.rent_car(name,id,car_name,deposit)
                                    except ValueError as v:
                                        print(v)
                                elif u_choice==4:
                                    try:
                                        u_name=input("\033[1m Enter Your Name 🪧 : \033[0m").upper()
                                        if not all( char.isalpha() or char.isspace() for char in u_name):
                                            raise ValueError("NAME SHOULD CONTAIN ALPHABETIC CHARACTERS")
                                        else:
                                            obj.return_car(u_name)
                                    except ValueError as v:
                                        print(v)
                                
                                else:
                                    print("EXITED")
                            break
                    else:
                        print("WRONG USERNAME AND PASSWORD")
            
            elif ch==3:
               pass
            
            else:
                break
                        
                    
        else:
            print("\t\t\t\t\033[1m ENTER VALID CHOICE \033[0m")
                        
                
            
            
        
        
            
            
            
