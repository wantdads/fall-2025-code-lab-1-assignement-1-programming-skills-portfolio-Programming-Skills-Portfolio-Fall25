# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user what name to search for
search_name = input("Enter the name to search for: ")

# Create a new list with all names in lowercase
lower_names = [name.lower() for name in names]

# See if lowercase input is in the lowercase list
if search_name.lower() in lower_names:
    print(search_name, "was found in the list!")
else:
    print(search_name, "was not found in the list.")
