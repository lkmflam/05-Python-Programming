def main():
    answer_key = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento", 
    "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", 
    "Idaho": "Boise", "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort", 
    "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis","Massachusetts": "Moston", "Michigan": "Lansing", "Minnesota": "Saint Paul", 
    "Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord", 
    "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhose Island": "Providence", "South Carolina": "Columbia", 
    "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier", "Virginia": "Richmond", 
    "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}
    count = 0
    amountcorrect = 0
    import random
    #Could make the test size however long here
    while count < 11:
        #Takes a random pair from the dictionary and stores in state
        state = random.choice(list(answer_key.items()))
        #Prints the actual state only and not the pair
        print(state[0])
        useranswer= input("Capital: ")
        #Compares the answer the user entered with the capital from the pair. If it isn't the same, it will not be added to correct answer count.
        if useranswer == state[1]:
            amountcorrect += 1
        else:
            pass
        count += 1
        #prints out the number of correct answers
    print(amountcorrect)
main()
