import random
def selectAnswer(wordList):
    location = random.randint(0,9)
    return wordList[location]
    #that takes a list of 5-letter words as an input parameter  and  returns  a  randomly  selected  5-letter  word  from  the  parameter  using  the random module.

def getInputFromUser():
    while True:
        print("Input 5 letters")
        user_input = input() 
        if user_input.islower():
            if len(list(user_input)) == 5:
                    return str(user_input)
            else:
                print(user_input + " is an invalid input. Try again.")
                print()
                continue             
        else:
            print(user_input + " is an invalid input. Try again.")
            print()
            continue
     
    #eturns a user-given 5-letter string satisfying the condition in game description 2. in str type.

def checkLetters(inputLetters):
    global random_word
    random_list = list(random_word)
    user_list = list(inputLetters)

    OutputList = ["0","0","0","0","0"] #[A, B, C, D, E]
    for a in range(5): #[H, E, L, L, O]
        for b in range(5): #[L, L, A, B, C]
            if user_list[a] == random_list[b]: #if first letter is in random list
                if user_list[a] == random_list[a]: #if letter is in the same position
                    OutputList[a] = "G"
                elif user_list[a] != random_list[a]: #if letter is not in the same position
                    OutputList[a] = "Y"
            elif user_list[a] != random_list[b]: #if letter is not in random list
                continue #continue until b is finished
        if OutputList[a] == "0":
            OutputList[a] = "B"
        else:
            continue
    return OutputList
    
    #takes the user-given 5-letter string as an input and returns the output as described in game description 4. 
    # The return value is a 5-letter string consists of ‘G’, ‘Y’, and/or ‘B’.

#MAIN CODE
WordList = ["apple", "bound", "nasty", "seven", "world", "piano", "green", "woman", "dream", "death"]
random_word = selectAnswer(WordList)
Try = 0
print("Wordle-like game starts!")
while Try < 6:
    Try += 1
    guessresult = ''.join(checkLetters(getInputFromUser()))
    print(guessresult)
    if guessresult == "GGGGG": #if guess is all correct
        print("You Win!")
        break
    elif Try == 6:
        print("You Lose! The word is {}.".format("".join(random_word)))
        break
    print()
