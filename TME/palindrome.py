#To check if the number is Palindrome
def is_palindrome(number):

    #Converts the number into a string
    return str(number) == str(number)[::-1]

#Process the file and check each line
def process_file(filename):

    #Opens the file and read all lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    #Loops each lline in the file
    for index, line in enumerate(lines, start=1):
        
        #Remove extra spaces and new lines
        numbers = line.strip().split(',')

        #Total Sum
        total_sum = sum(int(num) for num in numbers)

        #If the sum is a palindrome
        if is_palindrome(total_sum):
            # If the sum is a palindrome, print the result
            print(f"Line {index}: {','.join(numbers)} (sum {total_sum}) - Palindrome")
        else:
            #If the sum is not palindrome
            print(f"Line {index}: {','.join(numbers)} (sum {total_sum}) - Not a palindrome")

# Call the function with the name of the file
process_file('numbers.txt')             