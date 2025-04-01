#Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

#Concatenate names to form full name
full_name = first_name + " " + last_name

#Slice the first three characters of the first name
sliced_name = first_name[:7]

# Format greeting message
greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old."

#Display results
print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting_message)