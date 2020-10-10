# This program will demonstrate how we can write in a file.

# Write: This will delete existing data of the file and add new information

emp_file_write = open("employee_file.txt", "w")
emp_file_write.write("new employee list")
emp_file_write.close()

# Append
emp_file = open("employee_file.txt", "a")
emp_file.write("\n Yoda - HR \n Soda - Supervisor \n Koda - Developer \n Toda - Tester \n Boda - Business Analyst \n Aoda - Assistant manager")
emp_file.close()
