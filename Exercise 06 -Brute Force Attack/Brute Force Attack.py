# Correct password
correct_password = "12345"

# Number of attempts the user has
attempts = 5

# Keep asking until user is correct or runs out of attempts
while attempts > 0:
    entry = input("Enter the password: ")

    if entry == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

# If no attempts left
if attempts == 0:
    print("Maximum attempts reached. Authorities have been alerted.")
