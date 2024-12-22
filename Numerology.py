#Luis Silva Python 2 

class Numerology:
    def __init__(self, name, dob):
        # name and date of birth
        self.name = name
        self.dob = dob

    def getName(self):
        return self.name

    def getDOB(self):
        return self.dob

    def reduceToSingleDigit(self, num):
        # Reduce a number to a single digit
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    def getLifePathNumber(self):
        # Calculate Life Path Number from all digits in the date
        total = sum(int(char) for char in self.dob if char.isdigit())
        return self.reduceToSingleDigit(total)

    def getBirthDayNumber(self):
        # Extract and reduce the day from the date
        day = int(self.dob.split("-")[1])
        return self.reduceToSingleDigit(day)

    def getAttitudeNumber(self):
        # Sum the month and day, then reduce
        parts = self.dob.split("-")
        month = int(parts[0])
        day = int(parts[1])
        return self.reduceToSingleDigit(month + day)

    def letterToNumber(self, letter):
        # Map letters to numerology numbers
        letter = letter.upper()
        mapping = {1: "AJS", 2: "BKT", 3: "CLU", 4: "DMV", 5: "ENW",
                   6: "FOX", 7: "GPY", 8: "HQZ", 9: "IR"}
        for num, letters in mapping.items():
            if letter in letters:
                return num
        return 0

    def getSoulNumber(self):
        # Calculate Soul Number from vowels in the name
        vowels = "AEIOU"
        total = sum(self.letterToNumber(letter) for letter in self.name if letter.upper() in vowels)
        return self.reduceToSingleDigit(total)

    def getPersonalityNumber(self):
        # Calculate Personality Number from consonants in the name
        vowels = "AEIOU"
        total = sum(self.letterToNumber(letter) for letter in self.name if letter.upper() not in vowels and letter.isalpha())
        return self.reduceToSingleDigit(total)

    def getPowerNameNumber(self):
        # Combine Soul and Personality Numbers
        soul = self.getSoulNumber()
        personality = self.getPersonalityNumber()
        return self.reduceToSingleDigit(soul + personality)

    def __str__(self):
        # String representation of the object
        return (
            f"Numerology Report for {self.getName()}:\n"
            f"- Date of Birth: {self.getDOB()}\n"
            f"- Life Path Number: {self.getLifePathNumber()}\n"
            f"- Birth Day Number: {self.getBirthDayNumber()}\n"
            f"- Attitude Number: {self.getAttitudeNumber()}\n"
            f"- Soul Number: {self.getSoulNumber()}\n"
            f"- Personality Number: {self.getPersonalityNumber()}\n"
            f"- Power Name Number: {self.getPowerNameNumber()}"
        )
