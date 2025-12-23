
# convert txt file to array
textArr = []
try:
    with open('all_words.txt', 'r') as file:
        content = file.read()
        textArr = content.split("\n")
        
except FileNotFoundError:
    print("Error: The file was not found.")





def guessWord(textArray, correctWord):
    guessWord = "roses"
    valueSequence =[0,0,0,0,0]
    for i in range(0,len(guessWord)):
        print(i)

        if guessWord[i] == correctWord[i]:
            valueSequence[i] = 1
        elif guessWord[i] in correctWord and correctWord[i] != guessWord[i]:
            valueSequence[i] = 0
        else:
            pass
    return valueSequence

def checkArr(textArray, valueSequence):
        # 2. Build for loop here - terminate if word correct
    for word in textArr:
        pass
            
            # 3. Guess word analysed -> This will return an array with 5 elements that have values 0, 1, or 2. 0 = letter is grey(not in word), 1 = letter is here, 2 = right letter, must go somewhere else - index will be saved in a hashmap that links i.e iof word a was in letter 0, a -> 0)

            # 4. second for loop ->  if word[i] = 0 or (word[i] = 2 && i =  indexOfLetter) or word does not include all 2's, remove this letter.

            # continue until entire array covered.


print(guessWord(textArr, "rossa"))
print(textArr[0])