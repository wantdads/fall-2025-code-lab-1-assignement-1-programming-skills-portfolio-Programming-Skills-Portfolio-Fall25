# European Capitals Quiz

# Dictionary of countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki"
}

# Loop through each country
for country in quiz:
    answer = input("What is the capital of " + country + "? ")
    
    # Check the answer (ignoring capitalization)
    if answer.lower() == quiz[country].lower():
        print("Correct! Good job :)")
        print()  # blank line
    else:
        print("Wrong! The capital of", country, "is", quiz[country])
        print()  # blank line 




