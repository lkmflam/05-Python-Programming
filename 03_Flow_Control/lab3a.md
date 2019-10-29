|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Lab 3A

![](../.gitbook/assets/madlibs.png)

## General

Create your own mad libs game asking the user for input to fill in the blanks. Print out using .format\(\).

\(Humor encouraged\)

## Background

"Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story, before reading the – often comical or nonsensical – story aloud. The game is frequently played as a party game or as a pastime."

## Requirments

* Adhere to PEP8 \(Comments, formatting, style, etc\)
* Create a handfull of pharses that require different numbers of inputs
* Prompt the user for input\(s\):
  * Inputs can be done a number of ways... 
    * \(SIMPLE\) Ask user for input directly, tell them if the word\(s\) need to be a verb, noun, etc. 
    * \(Moderate\) Give the user a handful of choices per input to choose from.You will need to create a bank of verbs, nouns, etc for this. 
    * \(Harder\) Give the user cards based off the actual game. Allowing them to draw, etc following the rules. Allow them to only input those cards. 
  * \(opitional\) Implement basic user input checking:
    * Check to ensure words are words, numbers are numbers \(there are many ways to do this\)
    * Ensure symobls aren't used if they are not needed
    * Check length
    * etc
    * Implement re-input if input is incorrect
* Output the user inputs into the given pharse
* Use formatting to not only output the user inputs, but to create a UI within the terminal. Space out certain UI elements such as title of program, choices, menu deceration, etc. 

---

|[Next Topic](/03_Flow_Control/03_io_files.md)|
|---|

I was ----(verb) to ----(noun) when all of a sudden a -----(adjective) ---- (noun) came out of nowhere and ---- (verb) me.


main()
    print("You will now begin playing MadLibs! I will ask for you to print multiple words and all you have to do is follow the guidelines.")
    verb1 = input("Please enter your first verb. Always remember nothing inappropriate.")
    noun1 = input("Please enter your first noun.")
    adj1 = input("Please enter your first adjective.")
    noun2 = input("Please enter your second noun.")
    verb2 = input("Please enter your second verb.")
    escape = input(print("Do these all look correct? If not, please type "-1" to exit. {!s}, {!s}, {!s}, {!s}, {!s}".format(verb1, noun1, adj1, noun2, verb2)))
    escape = input
        if escape == -1 then 
        exit()
    print("I was {verb1} to {noun1} when all of a sudden a {adj1} {noun2}came out of nowhere and {verb2}ed me." .format(verb1, noun1, adj1, noun2, verb2))
exit()
