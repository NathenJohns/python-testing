# w = write
# a = append
# r = read
# r+ = read and write

employee_file = open("employees.txt", "a")
employee_file1 = open("employees1.txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()
employee_file1.close()
