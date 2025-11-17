# Ask the user for their info
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# Check if age is a number, if not ask one more time
if not age.isdigit():
    print("Please enter a number for age.")
    age = input("Enter your age again: ")

# If still not a number, set it to Unknown
if age.isdigit():
    age = int(age)
else:
    age = "Unknown"

# Store in a dictionary
bio = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Print the details
print("Name:", bio["Name"])
print("Hometown:", bio["Hometown"])
print("Age:", bio["Age"])
