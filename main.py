import random
import os
import shelve
# def main():
#   pass
# accounts = [[],[]]
# class Account:
#   def __init__(self, username, password,):
#     self.username = username
#     self.password = password
  
#   def LogIn(self, username, password):
#     if len(accounts[0]) > 0:
#       for i in range(len(accounts[0])):
#         if accounts[0][i] == username:
#           if accounts[1][i] == password:
#             global current
#             current = Account(username, password)
#             print("Logged In")
#             main()
#           else:
#             print("Incorrect Password")
            
#   def add_account(username, password):
#     if not username in accounts:
#       accounts[0].append(username)
#       accounts[1].append(password)
#     else:
#       print("Username taken")


Guesses = []

#random.choice chooses a random object from words list
wrong = 0
words = ['cat', 'dog', 'fish', 'lizard']
random_word = random.choice(words)
def ascii(x):
  if x == 0:
    os.system("clear")  
    print("Letters Guessed: " + str(Guesses))
  if x == 1:
    os.system("clear")
    print("Letters Guessed: " + str(Guesses))
    print
    return """
       __|__
       |   |
       O   |
          |
          |
          |
    ______|____
    You have 5 guesses left
    """
    

  elif x == 2:
     os.system("clear")
     print("Letters Guessed: " + str(Guesses))
     return """
       __|__
       |   |
       O   |
       |   |
          |
          |
    ______|____
    You have 4 guesses left
    """
  elif x == 3:
    os.system("clear")
    print("Letters Guessed: " + str(Guesses))
    return """
       __|__
       |   |
       O   |
      /|   |
          |
          |
    ____|_|____
    You have 3 guesses left
    """
  elif x == 4:
    os.system("clear")
    print("Letters Guessed: " + str(Guesses))
    return """
       __|__
       |   |
       O   |
      /|\  |
          |
          |
    ____|_|____
    You have 2 guesses left
    """
  elif x == 5:
    os.system("clear")
    print("Letters Guessed: " + str(Guesses))
    return """
       __|__
       |   |
       O   |
      /|\  |
      /    |
          |
    ______|____
    You have 1 guess left
    """
  elif x == 6:
    os.system("clear")
    print("Letters Guessed: " + str(Guesses))
    return """
       __|__
       |   |
       O   |
      /|\  |
      / \  |
          |
    ______|____

    YOU LOSE!
    """
    x = 0
    

def blank_word(word):
  return "_" * len(word)
def can_make_word(letters, word):
  sorted_letters = sorted(letters)
  sorted_word = sorted(word)
  j = 0
  for i in range(len(sorted_letters)):
    if j == len(sorted_word):
      return True
    if sorted_letters[i] == sorted_word[j]:
      j += 1
  return j == len(sorted_word)
  

  
def guess():
  # .lower() makes the input lowercase, therefore, we don't have to account for uppercase letters
  for i in random_word:
    if i in Guesses:
      print(i, end='')
    else:
      print("_", end='')
  input_letter  = input('<-Guess a letter:').lower()
  Guesses.append(input_letter)
  if input_letter in random_word:
    print(input_letter + " is in the word " + str(random_word.count(input_letter)) + "x")
  else:
    global wrong
    wrong += 1
  for i in random_word:
    if i in Guesses:
      print(i, end='')
    else:
      print("_", end='')
  print(" ")
  print(ascii(wrong))
  if wrong < 6:
    if can_make_word(Guesses,random_word):
      print(" YOU WIN!")
    else:
      retry()


#always a possibility from guess the word
def guess_word(word):
  if word.lower == random_word:
    print(" YOU WIN!")
  else: 
    global wrong
    wrong += 1 
    print(ascii(wrong))
    retry()
#^ this function doesn't work. Late now. will fix for sprint 2

#called after each major function as to continue the game as long as the function is within playing perameters -- hasn't won and hasn't lost
def retry():
  print("Would you like to:")
  print("1: Guess another letter")
  print("2: Guess the word")
  retry_query = input()
  if retry_query == '1':
    guess()
  elif retry_query == '2':
    word_guess = input("What do you think the word is? ")
    guess_word(word_guess)
guess()
  


