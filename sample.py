# with open('car.txt','r+') as fp:
#     lines=(fp.readlines())
#     for i,line in enumerate(lines):
#         data=line.split(' || ')
#         # print(data)
#         if (data[0]=='1'):
#             data[3]=input("Enter:")
#             lines[i]=' || '.join(data)+'\n'
#             fp.seek(0)
#             fp.writelines(lines)
#             print('data updated')

# print("""\n\n\t\t\t\t\t\t\033[1m=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n
#                     \t\t\t\t* 1.Add Cars             6.Rent Car             *\t\t\t\t\n
#                     \t\t\t\t* 2.Display Cars         7.Return Car           *\t\t\t\t\n
#                     \t\t\t\t* 3.Search Cars          8.Display Rented Cars  *\t\t\t\t\n
#                     \t\t\t\t* 4.Delete Cars          9.Display Return Cars  *\t\t\t\t\n
#                     \t\t\t\t* 5.Update Cars          10.Exit                *\t\t\t\t\n
#                     \t\t\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\033[0m\t\t\t\t
#     """)
# import re
# try:
#     reg_no=input("\033[1m Enter Reg No: \033[0m").capitalize()
#     if not re.match(r'^[A-Z]{2}\d{2}\s?[A-Z]{1,2}\s?\d{1,4}$', reg_no):
#             raise ValueError("Invalid registration number format. Example format: AB12 CD 1234")
#     print(reg_no ,"Success")
# except ValueError as v:
#     print(v)


# ask=input("ENTER CAR ID:")
# filter_data=''
# with open('Rented.txt','r') as fp:
#     read=fp.readlines()
#     filter_data=[d for d in read if ask not in d  ]
# with open('Rented.txt','w') as f:
#     f.writelines(filter_data)
#     print("DATA UPDATED")
# u_name=input("ENTER YOUR NAME:").upper()
# with open ('Rented.txt','r') as fp:
#             for i in fp:
#                if u_name in i:
#                     print(i)

# try:
#    username = input("\033[1mEnter Your Username:\033[0m").strip()
#    if not all(char.isalpha() or char.isspace() for char in username):
#       raise ValueError("Username should contain only alphabetic characters and spaces.")
# except ValueError as v:
#     print(v)
# import random as rd
# avail=5
# no_list=[]
# series='MH',"HR",'PN',"TN","UP"
# for j in range(avail):
#    for k in series:
#     no_list.append(series)
#    no=random.randint(1000,9999)
#    if no in no_list:
#       pass
#    else:
#       no_list.append(no)
# print(no_list)

# import random as rd

# avail = 5
# num = ["MH 13" + " HR " + str(i)*2 + " " + str(rd.randint(1000, 9999)) for i in range(1, avail + 1)]

# print(num)

import ast
import random
car_name=input("ENTER CAR NAME:").upper()
# Open the file
with open('cars.txt', 'r') as f:
   for k in f:
      split_txt=k.split(' || ')
      if split_txt[0]==car_name:
      # Extract the list part and convert it to a Python list
         list_part = split_txt[4].strip()
         car_list = ast.literal_eval(list_part)

         # Get some random numbers from the list
         # random_numbers = random.sample(car_list, k=1)  # Change k to the number of random numbers you want

         # Print the random numbers
         print("Random numbers from the list:")
         u_num=input("Enter car num:")
         for number in car_list:
            if u_num in number:
               print(number)
               
         else:
            print("Not Found")
            
