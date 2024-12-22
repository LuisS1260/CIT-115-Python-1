#Luis Silva Python 2

from Numerology import Numerology

def main():
    # Get user input for name and date of birth
    name = input("Enter your full name: ").strip()
    dob = input("Enter your date of birth (mm-dd-yyyy): ").strip()

    # Validate input
    if not name:
        print("Name cannot be empty.")
        return
    if len(dob) != 10 or not dob.replace("-", "").isdigit():
        print("Date of birth must be in the format mm-dd-yyyy.")
        return

    # Create Numerology object
    numerology = Numerology(name, dob)

    # Use __str__ to display the full report
    print("\n" + str(numerology))

if __name__ == "__main__":
    main()
