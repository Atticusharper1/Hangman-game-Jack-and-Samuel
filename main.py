import random
import os
import shelve

accounts = [[],[]]
with shelve.open('accounts') as db:
  if "accounts" in db:
    accounts = db['accounts']
    
class Account:
  def __init__(self, username, password,):
    self.username = username
    self.password = password

  def LogIn(username, password):
    if len(accounts[0]) > 0:
      for i in range(len(accounts[0])):
        if accounts[0][i] == username:
          if accounts[1][i] == password:
            global current
            current = Account(username, password)
            print("Logged In")
            main()
          else:
            print("Incorrect Password")
            
  def add_account(username, password):
    if not username in accounts:
      accounts[0].append(username)
      accounts[1].append(password)
      with shelve.open('accounts') as db:
        db['accounts'] = accounts
      print("Account Created")
    else:
      print("Username taken")
    


def main():
  words = ['cat', 'dog', 'fish', 'lizard']
  class Game:
    def __init__(self, random_word, guesses, wrong):
      self.wrong = wrong
      self.random_word = random_word
      self.guesses = guesses
    
    def return_letters_found(self):
      for i in self.random_word:
        if i in self.guesses:
          print(i, end='')
        else:
          print("_", end='')
          
    def ascii(self):
      if self.wrong == 0:
        os.system("clear")  
        print("Letters Guessed: " + str(self.guesses))
        self.return_letters_found()
        print(" ")
        print( """
               _
             _[_]_
              (")
          `--( : )--'
            (  :  )
            `-...-'
        You still have 6 guesses
        """)
        return(" ")
      elif self.wrong == 1:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print(" ")
          print( """
                 _
                (")
            `--( : )--'
              (  :  )
              `-...-'
          You have 5 guesses left
          """)
          return(" ")
      elif self.wrong == 2:
           os.system("clear")
           print("Letters Guessed: " + str(self.guesses))
           self.return_letters_found()
           print( """
                 _
                (")
               ( : )--'
              (  :  )
              `-...-'
          You have 4 guesses left
          """)
           return(" ")
      elif self.wrong == 3:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
               ( : )
              (  :  )
              `-...-'
          You have 3 guesses left
          """)
          return(" ")
      elif self.wrong == 4:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
               ( : )
               
          You have 2 guesses left
          """)
          return(" ")
      elif self.wrong == 5:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
  
          You have 1 guess left
          """)
          return(" ")
      elif self.wrong == 6:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
          YOUR SNOWMAN MELTED
  
          YOU LOSE!
          """)
          return(" ")
          self.wrong = 0
        
    def blank_word(self):
      return "_" * len(self.random_word)

    def can_make_word(self, letters):
      sorted_letters = sorted(letters)
      sorted_word = sorted(self.random_word)
      j = 0
      for i in range(len(sorted_letters)):
          if j == len(sorted_word):
              return True
          if sorted_letters[i] == sorted_word[j]:
              j += 1
      return j == len(sorted_word)
  
    def guess(self):
        # .lower() makes the input lowercase, therefore, we don't have to account for uppercase letters
        self.return_letters_found()
        input_letter  = str(input('Guess a letter: ').lower())
        if input_letter in self.guesses:
            print("Letter already guessed!")
            self.retry()
        if input_letter in self.random_word:
            self.guesses.append(input_letter)
            print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
            self.retry()
        else:
            print(input_letter + " is not in the word")
            self.wrong += 1
            self.retry()
        if self.can_make_word(self.guesses) == True:
            print("You Win!")
            return True
        else:
            return False
    def retry(self):
        input_letter  = input('Guess a letter again: ').lower()
        if input_letter in self.guesses:
            print("Letter already guessed!")
     
        else:
            self.guesses.append(input_letter)
            if input_letter in self.random_word:
                print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
                
            else:
                print(input_letter + " is not in the word")
               
  # creating an instance of the class
  game = Game(random.choice(words), [], 0)
  game.ascii()
  game.guess()



choice = int(input("Would you like to 1: log in or 2: make an account? "))
if choice == 1:
  username = str(input("Username: "))
  password = str(input("Password: "))
  Account.LogIn(username,password)
if choice == 2:
  username = str(input("Username: "))
  password = str(input("Password: "))
  Account.add_account(username, password)import random
import os
import shelve

accounts = [[],[]]
with shelve.open('accounts') as db:
  if "accounts" in db:
    accounts = db['accounts']
    
class Account:
  def __init__(self, username, password,):
    self.username = username
    self.password = password

  def LogIn(username, password):
    if len(accounts[0]) > 0:
      for i in range(len(accounts[0])):
        if accounts[0][i] == username:
          if accounts[1][i] == password:
            global current
            current = Account(username, password)
            print("Logged In")
            main()
          else:
            print("Incorrect Password")
            
  def add_account(username, password):
    if not username in accounts:
      accounts[0].append(username)
      accounts[1].append(password)
      with shelve.open('accounts') as db:
        db['accounts'] = accounts
      print("Account Created")
    else:
      print("Username taken")
    


def main():
  words = ['cat', 'dog', 'fish', 'lizard']
  class Game:
    def __init__(self, random_word, guesses, wrong):
      self.wrong = wrong
      self.random_word = random_word
      self.guesses = guesses
    
    def return_letters_found(self):
      for i in self.random_word:
        if i in self.guesses:
          print(i, end='')
        else:
          print("_", end='')
          
    def ascii(self):
      if self.wrong == 0:
        os.system("clear")  
        print("Letters Guessed: " + str(self.guesses))
        self.return_letters_found()
        print(" ")
        print( """
               _
             _[_]_
              (")
          `--( : )--'
            (  :  )
            `-...-'
        You still have 6 guesses
        """)
        return(" ")
      elif self.wrong == 1:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print(" ")
          print( """
                 _
                (")
            `--( : )--'
              (  :  )
              `-...-'
          You have 5 guesses left
          """)
          return(" ")
      elif self.wrong == 2:
           os.system("clear")
           print("Letters Guessed: " + str(self.guesses))
           self.return_letters_found()
           print( """
                 _
                (")
               ( : )--'
              (  :  )
              `-...-'
          You have 4 guesses left
          """)
           return(" ")
      elif self.wrong == 3:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
               ( : )
              (  :  )
              `-...-'
          You have 3 guesses left
          """)
          return(" ")
      elif self.wrong == 4:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
               ( : )
               
          You have 2 guesses left
          """)
          return(" ")
      elif self.wrong == 5:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
                 _
                (")
  
          You have 1 guess left
          """)
          return(" ")
      elif self.wrong == 6:
          os.system("clear")
          print("Letters Guessed: " + str(self.guesses))
          self.return_letters_found()
          print("""
          YOUR SNOWMAN MELTED
  
          YOU LOSE!
          """)
          return(" ")
          self.wrong = 0
        
    def blank_word(self):
      return "_" * len(self.random_word)

    def can_make_word(self, letters):
      sorted_letters = sorted(letters)
      sorted_word = sorted(self.random_word)
      j = 0
      for i in range(len(sorted_letters)):
          if j == len(sorted_word):
              return True
          if sorted_letters[i] == sorted_word[j]:
              j += 1
      return j == len(sorted_word)
  
    def guess(self):
        # .lower() makes the input lowercase, therefore, we don't have to account for uppercase letters
        self.return_letters_found()
        input_letter  = str(input('Guess a letter: ').lower())
        if input_letter in self.guesses:
            print("Letter already guessed!")
            self.retry()
        if input_letter in self.random_word:
            self.guesses.append(input_letter)
            print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
            self.retry()
        else:
            print(input_letter + " is not in the word")
            self.wrong += 1
            self.retry()
        if self.can_make_word(self.guesses) == True:
            print("You Win!")
            return True
        else:
            return False
    def retry(self):
        input_letter  = input('Guess a letter again: ').lower()
        if input_letter in self.guesses:
            print("Letter already guessed!")
     
        else:
            self.guesses.append(input_letter)
            if input_letter in self.random_word:
                print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
                
            else:
                print(input_letter + " is not in the word")
               
  # creating an instance of the class
  game = Game(random.choice(words), [], 0)
  game.ascii()
  game.guess()



choice = int(input("Would you like to 1: log in or 2: make an account? "))
if choice == 1:
  username = str(input("Username: "))
  password = str(input("Password: "))
  Account.LogIn(username,password)
if choice == 2:
  username = str(input("Username: "))
  password = str(input("Password: "))
  Account.add_account(username, password)
