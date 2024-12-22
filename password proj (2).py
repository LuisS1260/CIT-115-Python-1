def main():
 # Get the user's full name
    sName = input("Please enter your First and Last name: ")
    
# prompt until correct password is given
    while True:
        sPassword = input("Please create your password: ")
        
#initials
        first_name, last_name = sName.split()
        sInitials = first_name[0] + last_name[0]
        
#validate the password length
        if not (8 <= len(sPassword) <= 12):
            print("Error: Password must be between 8 and 12 characters.")
            continue
        
#checking starting characters
        if sPassword.startswith("Pass") or sPassword.startswith("pass"):
            print("Error: Password can’t start with Pass.")
            continue
        
#looking for one uppercase
        if not any(char.isupper() for char in sPassword):
            print("Error: Password must contain at least 1 uppercase letter.")
            continue
        
#looking for lowercase
        if not any(char.islower() for char in sPassword):
            print("Error: Password must contain at least 1 lowercase letter.")
            continue
        
#looking for one number
        if not any(char.isdigit() for char in sPassword):
            print("Error: Password must contain at least 1 number.")
            continue
        
# checking for special characters
        special_characters = "!@#$%^"
        if not any(char in special_characters for char in sPassword):
            print("Error: Password must contain at least 1 of these special characters: ! @ # $ % ^")
            continue
        
# initials 
        if sInitials.lower() in sPassword.lower():
            print("Error: Password must not contain your initials.")
            continue
        
# looking for duplicate characters
        character_count = {}
        duplicates_found = False
        
        for char in sPassword:
            lower_char = char.lower()
            if lower_char in character_count:
                character_count[lower_char] += 1
                duplicates_found = True
            else:
                character_count[lower_char] = 1
        
        if duplicates_found:
            print("These characters appear more than once:")
            for char, count in character_count.items():
                if count > 1:
                    print(f"{char}: {count}")
            continue
        
#  All checks passed
        print("Success: Password is valid and OK to use.")
        break

# main function
if __name__ == "__main__":
    main()
