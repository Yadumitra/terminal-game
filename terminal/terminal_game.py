import random
import time
import sys

def print_slow(text):
    """Prints text slowly for dramatic effect."""
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def welcome_message():
    print_slow("Welcome to Your Daily Routine!")
    print_slow("It's 7 in the morning. Choose your routine for the day.")
    print_slow("Good luck!\n")

def morning_choice():
    print_slow("1. Wake up")
    print_slow("2. Sleep more")
    choice = input("Choose an option (1 or 2): ")

    if choice == "2":
        print_slow("\nYou chose to sleep more...  The day is wasted. GAME OVER.")
        sys.exit()
    else:
        print_slow("\nGood choice! You woke up early.")
        print_slow("What do you want to do next?")
        print_slow("1. Go for a walk")
        print_slow("2. Have breakfast")
        print_slow("3. Sleep again")

        while True:
            choice = input("Choose an option (1-3): ")
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print_slow("Invalid choice, please try again.")

def go_for_walk():
    print_slow("\nYou head out for a refreshing walk...")
    events = [
        "You meet a friendly dog and pet it. Happiness +10 ",
        "You trip on a rock. Ouch. HP -50xp.",
        "You find a ₹500 note on the ground. Lucky day! +50xp",
        "You breathe fresh air and feel amazing! +30xp",
        "You see a beautiful sunrise. Nature's beauty +20xp",
    ]
    print_slow(random.choice(events))
    print_slow("You return home energized. +30xp")

def have_breakfast():
    print_slow("\nYou sit down for breakfast...")
    meals = [
        "You eat healthy oats and fruits. Energy +20!",
        "You devour pancakes with syrup. Yum, but sugar rush incoming! -10xp",
        "You spill coffee on your shirt. Not great... -20xp"
    ]
    print_slow(random.choice(meals))
    print_slow("You feel ready to take on the day!")

def sleep_again():
    print_slow("\nYou chose to sleep again... The bed pulls you into a black hole of laziness. -100xp")
    print_slow("By the time you wake up, it's evening. Day wasted. GAME OVER.")
    sys.exit()

def afternoon_adventure():
    print_slow("\nIt's now afternoon. What do you want to do?")
    print_slow("1. Work on your projects ")
    print_slow("2. Watch Netflix ")
    print_slow("3. Call your best friend ")
    
    while True:
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            print_slow("\nYou worked hard and made great progress! Future you is proud. +50xp")
        elif choice == "2":
            print_slow("\nYou binge-watch a whole season. Productive? Nope. Fun? Yup. -10xp")
        elif choice == "3":
            print_slow("\nYou laugh for hours with your friend. Mood boosted! +20xp")
        else:
            print_slow("Invalid choice, try again.")
            continue
        break
def evening_choice():
    print_slow("\nEvening is here. What do you want to do?")
    print_slow("1. Go out with friends")
    print_slow("2. Read a book")
    print_slow("3. Do Nothing, just relax")
    num=int(input("Choose an option (1-3): "))
    if num not in [1, 2, 3]:
        print_slow("Invalid choice, try again.")
        return evening_choice()

    while True:
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            print_slow("\nYou have a blast with your friends! +40xp")
        elif choice == "2":
            print_slow("\nYou read an inspiring book. Knowledge +30xp")
        elif choice == "3":
            print_slow("\nYou prepare for tomorrow, feeling accomplished. +20xp")
        else:
            print_slow("Invalid choice, try again.")
            continue
        break

def play_game():
    welcome_message()
    morning = morning_choice()
    
    if morning == 1:
        go_for_walk()
    elif morning == 2:
        have_breakfast()
    else:
        sleep_again()

    afternoon_adventure()
    evening_choice()
    print_slow("\nNight falls... You feel good about your day. THE END.")

if __name__ == "__main__":
    play_game()
