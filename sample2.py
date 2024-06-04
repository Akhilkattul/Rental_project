import ast

# Take input from the user for the car name
car_name = input("ENTER CAR NAME:").upper()

# Open the file
with open('cars.txt', 'r') as f:
    lines = f.readlines()  # Read all lines into a list

# Flag to indicate if the input is found
found = False

# Iterate through the lines and find the car name
for i in range(len(lines)):
    # print(i)
    split_txt = lines[i].split(' || ')
    if split_txt[0] == car_name:
        # Extract the list part and convert it to a Python list
        list_part = split_txt[4].strip()
        car_list = ast.literal_eval(list_part)

        # Take input from the user to search in the car list
        user_input = input("Enter car number to search:")

        # Iterate through the car_list and check if the user input is present
        for j in range(len(car_list)):
            if user_input == car_list[j]:
                found = True
                new_no=car_list[j]
                # Replace the found value with "NA" in the car list
                car_list[j] = "NA"+ new_no

                # Update the line with the modified car list
                lines[i] = split_txt[0] + ' || ' + split_txt[1] + ' || ' + split_txt[2] + ' || ' + split_txt[3] + ' || ' + str(car_list) + '\n'

                # Write the modified lines back to the file
                with open('cars.txt', 'w') as f:
                    f.writelines(lines)

                print("FOUND")
                break
        else:
            print("Car number is not present.")
        break
else:
    print("Car not found.")
# with open ("rc.txt",'a') as fp:
#     user="Akhil" 
#     fp.writelines(f"{user} | {new_no}"+"\n") 
#     print("DATA ENTERED")
                
           
                
            


# import ast
# file = "car.txt"
# with open(file,'r+')as file:
#     car_data = file.readlines()
#     for data  in car_data:
#         split_data = data.split("||")
#         ldata = (split_data[4].strip())
#         num_list = ast.literal_eval(ldata)
#         print(num_list)
#         rent_car = int(input("Enter Car index   to rent the car: "))
#         Rented_car = num_list[rent_car]
#         num_list[rent_car] = ""
#         split_data[4] = str(num_list)
#         car_data[car_data.index(data)] = "||".join(split_data) +"\n" 
#         file.seek(0)
#         file.writelines(car_data)
#         print(f"Car data updated ! rented Car number is {Rented_car}")