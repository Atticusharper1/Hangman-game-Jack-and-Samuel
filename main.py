import random

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

global wrong 
correct_guesses = []
wrong_guesses = []
wrong = 0
words = ['cat', 'dog', 'fish', 'lizard']
def guess(x):
  random_word = random.choice(words)
  print(random_word)
  blanked_random_word = "_" * len(random_word)
  print(blanked_random_word)
  if x in random_word:
      correct_guesses.append(x)
  else:
    global wrong
    wrong+=1
    wrong_guesses.append(x)
    print(ascii(wrong))

  

guess("b")

def ascii(wrong):
  if wrong == 1:
    return """
       __|__
       |   |
       O   |
          |
          |
          |
    ______|____
    """
  if wrong == 2:
     return """
       __|__
       |   |
       O   |
       |   |
          |
          |
    ______|____
    """
  if wrong == 3:
     return """
       __|__
       |   |
       O   |
      /|   |
          |
          |
    ____|_|____
    """
  if wrong == 4:
    return """
       __|__
       |   |
       O   |
      /|\  |
          |
          |
    ____|_|____
    """
  if wrong == 5:
    return """
       __|__
       |   |
       O   |
      /|\  |
      /    |
          |
    ______|____
    """
  if wrong == 6:
    return """
       __|__
       |   |
       O   |
      /|\  |
      / \  |
          |
    ______|____
    """
    wrong = 0
