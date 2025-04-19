# Function to display menu and get user selection
def sel():
    print("\nMain Menu:")
    print("1. Do you want to suggest a place?")
    print("2. Do you want to suggest what we need to fix in a place?")
    print("3. Do you want to suggest ways to help people in need?")
    
    try:
        selection = int(input("Please enter your selection (1-3): "))
        if selection in [1, 2, 3]:
            return selection
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            return sel()
    except ValueError:
        print("Please enter a valid number.")
        return sel()

# Function to calculate and print average of a list
def average(list1):
    if len(list1) == 0:
        print("List is empty. Cannot calculate average.")
        return None
    avg = sum(list1) / len(list1)
    print(f"Average: {avg}")
    return avg

# Survey function to check if a country is in need and save the result
def whichCountry():
    try:
        w = int(input("How many liters of water does a person get per day? "))
        h = float(input("How far (in kilometers) does the person need to travel for water? "))
        if w < 10 or h > 2:
            country = input("Which country is that? ")
            print("Thanks for suggesting " +country+". We are needed to help them.")
            with open("countries_in_need.txt", "a") as file:
                file.write("Country: "+country+", Water per day: "+str(w)+"L, Distance: "+str(h)+"km\n")

        else:
            print("Thank you. This does not seem like an emergency, but we'll keep it noted.")
    except ValueError:
        print("Please enter valid numerical values.")
        whichCountry()

# Function to save general suggestions to file
def saveSuggestion(suggestion):
    with open("suggestions.txt", "a") as file:
        file.write(suggestion.strip() + "\n")

# Displays current research and solutions
def display():
    print("\nCurrent Research and Solutions:")
    print("- A water source tracker within a 10km radius, solar-chargeable.")
    print("- Healing ointment for insect bites, burns, and emergency medical kits for diarrhea, fever, and cold.")
    print("- A 'magic glue' that bonds leaves to form pitchers.")
    print("- A UV-torch based water purifier that kills bacteria and microbes.")

# Main function
def main():
    s = sel()
    if s == 1:
        whichCountry()
    else:
        suggestion = input("Please give us your suggestions: ")
        print("Thank you for your suggestion. We will research this and try to incorporate it into our system.")
        saveSuggestion(suggestion)
    display()

main()
