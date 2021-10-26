

def guessingGame(secret_word,guesses_allowed = 5):

  guess = ""
  guess_count = 1

  while secret_word != guess:
    guess = input("Please enter your guess of the secret word: ")
    if guess == secret_word:
      print("You got it. The word was " + secret_word + " and it took you " + str(guess_count) + " guesses.")
      return
    if guess_count >= guesses_allowed:
      print("Sorry you lost! The secret word was " + secret_word)
      return
    else:
      guess_count += 1
  
guessingGame("llama")