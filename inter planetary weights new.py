import pickle  # Import the pickle module for saving and loading data

dictPlanetGravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066
}

def main():
    #dictionary to hold the history of entered weights. 
    dictPlanetHistory = {}

    # name of the file to save previous data
    sFileName = 'ls_PlanetaryWeights.db'
    
    # Trying to load previous data from the pickle file
    try:
        with open(sFileName, 'rb') as f:  
            dictPlanetHistory = pickle.load(f)  
    except FileNotFoundError:
        print("No previous weight history found. Starting fresh.")  

    # Ask the user if they want to see previous entries
    sViewHistory = input("Would you like to see the previous entries? (Y/N): ").strip().lower()
    if sViewHistory == 'y':
        if dictPlanetHistory:  
            print("Previous Entries:")
            for sName, dictWeights in dictPlanetHistory.items():  
                print(f"{sName}: {dictWeights}") 
        else:
            print("No previous entries found.")  

 # Start a loop for user input
    while True:
        # Ask for a unique name
        sName = input("Enter a unique name (or press Enter to exit): ").strip()
        if not sName:  
            break
        
 # Check to see if the name already exists in the history
        sLowerName = sName.lower()
        if sLowerName in (key.lower() for key in dictPlanetHistory.keys()):
            print("Name already exists. Please enter a different unique name.")  
            continue  

     # Get a valid Earth weight from the user
        while True:
            try:
                fEarthWeight = float(input("Enter your Earth weight: "))  
                break  
            except ValueError:
                print("Invalid input. Please enter a numeric value.")  

        # Create a dictionary for the person's weights on different planets
        dictPersonWeights = {}

        # Calculate weights on each planet
        for sPlanet, fGravity in dictPlanetGravity.items():  
            fPlanetWeight = fEarthWeight * fGravity  
            dictPersonWeights[sPlanet] = fPlanetWeight  

        # Add the person's weights to the history dictionary
        dictPlanetHistory[sName] = dictPersonWeights

        # results
        print(f"\n{sName}'s Solar System's Weights:")  
        for sPlanet, fWeight in dictPersonWeights.items():  
            print(f"{sPlanet:>10}: {fWeight:10.2f}")  

    # Save the updated history back to the pickle file
    with open(sFileName, 'wb') as f:  
        pickle.dump(dictPlanetHistory, f)  

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
