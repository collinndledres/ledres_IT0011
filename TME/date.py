from datetime import datetime

#Ask the user to enter a date in mm/dd/yyyy format
date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    #Convert the input string into a datetime object
    date_object = datetime.strptime(date_input, "%m/%d/%Y")

    #Convert the date into a human-readable format
    formatted_date = date_object.strftime("%B %d, %Y")

    #Display the result
    print(f"Date Output: {formatted_date}")

except ValueError:
    # Handle cases where the input format is incorrect
    print("Invalid date format! Please enter the date in mm/dd/yyyy format.")