def read_student_info():
    try:
        #Open the file in read mode
        with open('students.txt', 'r') as file:
            print("Reading Student Information:\n")
            # Read and display file contents
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file 'students.txt' was not found.")

#Execute the function
read_student_info()