# This code will demonstrate how to read files in python

emp_file = open("employee_file_read.txt", "r")

# Check if the file is readable or not

print(emp_file.readable())

# Read first line. Once this command run cursor be on second line and we can read that by writing same command.
line = emp_file.readline()
print(line)
print(emp_file.readline())

# Read all lines: this method returns all lines in list
print(emp_file.readlines())

# Read whole file, this does not work if used after readline method and vice versa.
print(emp_file.read())

emp_file.close()
