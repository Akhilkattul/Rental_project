# from tabulate import tabulate

# table = []  # Initialize table outside the loop
# headers = ["CAR ID", "NAME","PROOF","CAR NAME","RENTED DATE", "RETURN DATE","TOTAL BILL"]

# with open('Rented.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         split_Text = line.strip().split(' || ')
#         table.append(split_Text)  # Add each row to the table

# print(tabulate(table, headers=headers, tablefmt="psql"))
# import random
# from datetime import datetime
# def rent_car(self,name,id,car_name,Deposit):
#         car_rand_id=random.randint(0,1000)
#         # car_id=str(int(input("Enter Car Id:"))
#         list=[]
#         found=False
#         with open('car.txt','r') as fp:
#             for i in fp:
#                 splited_text=i.split(' || ')
#                 if (str(car_name) in str(splited_text[0])) and (str(splited_text[3])>str(0)):
#                     found=True
#                     splited_text[3]=str(int(splited_text[3])-1)
#                     splited_text[4]=str(int(splited_text[4])+1)
#                     i=" || ".join(splited_text)+'\n'
#                     list.append(i)
                    
                    
#                     rent_date=input("\033[1m ENTER DATE(DD-MM-YYYY) 📅:\033[0m") #User date
#                     date_1=datetime.datetime.strptime(rent_date,"%d-%m-%Y")
#                     date_2=date_1.date()
#                     date_3=date_2.strftime('%d-%m-%Y')
                                    

#                     with open ("Rented.txt",'a') as f:
#                         f.write(f"{car_rand_id} || {name} || {id} || {car_name} || {date_3} || NA || 0 || {Deposit}"+'\n')
#                         print(f"\n\n CAR RENTED SUCCESSFULLY ✅")  
#                 else:
#                     list.append(i)
#         if found==True:
#           with open('car.txt','w') as fp:
#               for x in list:
#                   fp.write(x)
                  
#         else:
#             print("Car Not Found Enter valid car Name") 

import ast
# Take input from the user for the car name
car_name = input("ENTER CAR NAME:").upper()
# Open the file
with open('cars.txt', 'r') as f:
    lines = f.readlines()  # Read all lines into a list


found = False

# Iterate through the lines and find the car number
for i in range(len(lines)):
    split_txt = lines[i].split(' || ')
    if split_txt[0] == car_name:
        list_part = split_txt[4].strip()
        car_list = ast.literal_eval(list_part)
        # Take input from the user to return the car
        returned_car = input("Enter car number to return:")

    # Check if the returned car number is in the car list and marked as "NA"
        for j in range(len(car_list)):
            if 'NA'+returned_car in car_list[j]:
                found = True
                # Remove "NA" from the list
                car_list[j] = returned_car

                # Update the line with the modified car list
                lines[i] = split_txt[0] + ' || ' + split_txt[1] + ' || ' + split_txt[2] + ' || ' + split_txt[3] + ' || ' + str(car_list) + '\n'

                # Write the modified lines back to the file
                with open('cars.txt', 'w') as f:
                    f.writelines(lines)

                print("Car returned successfully.")
                break
        else:
                print("Car number is not present.")
        break
else:
    print("Car not found or already returned.")

