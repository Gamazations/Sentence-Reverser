def reverse_sentence(sentence):
  #Splits the inputted sentence from the user using a parameter into word by word, and stores it into a list called words
  words = sentence.split()

  #Checks to ensure the list of words is more than one word, if it is not, returns the value inputted as they only put one word and this does not need to be reversed
  if len(words)<=1:
    return sentence

  #Else, it continues with recursion to reverse the sentence.
  else:
  #This accesses the rest of the words aside from the first one, accessing the 2nd index of the list. 
    restOfSentence = ' '.join(words[1:])
    #This reverses the rest of the sentence recursively.
    reverseRestOfSentence = reverse_sentence(restOfSentence)
    #This finally combines the newly reversed sentence using recursive functions and then adds the last word back to the end.
    finalReversedSentence = reverseRestOfSentence + ' ' + words[0]
    #Then finally, it returns the value of the reversed sentence.
    return finalReversedSentence

#Asks the user for the initial input
sentenceInput = input("Type a sentence that you want to reverse!: ")
#Formats the output of the reversed sentence in a print statement and a nice way for the user to view.
print("The reversed version of this sentence is:", reverse_sentence(sentenceInput))

#EXTRA: Asks user if they want the letters reversed of their sentence as well
wantToReverseWords = input("Do you want to reverse the letters of your sentence as well? (Y/N): ")
#If yes, converts user input into a list, uses .reverse() to reverse the letter order, and joins the list back into a string to be printed to the user.
if wantToReverseWords == "Y":
  listOfLetters = list(sentenceInput)
  listOfLetters.reverse()
  reversedLetters = ''.join(listOfLetters)
  print("The sentence with the letters reversed is:", reversedLetters)
#If not, prints a have a good day message for the user.
else:
  print("Have a good day!")
  
