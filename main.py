import random
import os
import shelve

accounts = [[],[]]
saved_games = []
game_over = False

class Account:
  ## Class Account attributes are username and password
  def __init__(self, username, password,):
    self.username = username
    self.password = password

  def LogIn(username, password):
    with shelve.open('accounts') as db:
      if "accounts" in db:
        accounts = db['accounts']
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
        else: 
            print("Username Not Found")
            start_menu()
            
            
  def add_account(username, password):
    if not username in accounts:
      accounts[0].append(username)
      accounts[1].append(password)
      with shelve.open('accounts') as db:
        db['accounts'] = accounts
      print("Account Created")
    else:
      print("Username taken")
class Game:
    def __init__(self, random_word, guesses, wrong):
      self.wrong = wrong
      self.random_word = random_word
      self.guesses = guesses
    #crux of the hangman code. It makes it so that the word is blanked according to the letters guessed.
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
      You have 6 guesses
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
          game_over = True
          ## Removes game from saved_games list
          saved_games.pop(game_choice - 1)
          ## Removes game from shelve of games
          with shelve.open('games') as db:
            if "games" in db:
              db['games'] = saved_games
          print('The word was ' + self.random_word)
          exit()
          return(" ")
    
        
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
        # self.return_letters_found()
        self.ascii()
        input_letter  = str(input('Guess a letter: ').lower())
        if input_letter == "end":
          saved_games.append(game)
          with shelve.open('games') as db:
            if "games" in db:
              db['games'] = saved_games
          exit()
          
        if input_letter in self.guesses:
            print("Letter already guessed!")
            self.retry()
        if input_letter in self.random_word:
            self.guesses.append(input_letter)
            print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
        
            self.retry()
        else:
            self.guesses.append(input_letter)
            print(input_letter + " is not in the word")
            self.wrong += 1
            self.retry()
        if self.can_make_word(self.guesses) == True:
            print("You Win!")
            game_over = True
            if game_over == True:
              saved_games.pop(game_choice - 1)
              with shelve.open('games') as db:
                if "games" in db:
                  db['games'] = saved_games
                  exit()
            
            return True
        else:
            return False
    def retry(self):
        self.ascii()
        input_letter  = input('Guess a letter again: ').lower()
        #when end is inputted it will save the game to saved games in db so it can be accessed and played later.
        if input_letter == "end":
          saved_games.append(game)
          with shelve.open('games') as db:
            if "games" in db:
              print(saved_games)
              db['games'] = saved_games
          exit()
        if input_letter == "hint":
          print(random.choice(self.random_word))
          self.retry()
        if input_letter in self.guesses:
            print("Letter already guessed!")
            self.retry()
        else:
            self.guesses.append(input_letter)
            if input_letter in self.random_word:
                print(input_letter + " is in the word " + str(self.random_word.count(input_letter)) + "x")
                if self.can_make_word(self.guesses) == True:
                  game_over = True
                  print("You Win!!")
                  #removes the game object from active games that are presented at the start of the program. 
                  saved_games.pop(game_choice - 1)
                  with shelve.open('games') as db:
                    if "games" in db:
                      db['games'] = saved_games
                  exit()
                else:
                  self.retry()
                
            else:
                print(input_letter + " is not in the word")
                self.wrong += 1
                self.retry()
  # creating an instance of the class
 


def main():
  global saved_games
  words =["abruptly","absurd","abyss","affix","askew","avenue","awkward","azure","bagpipes","bandwagon","banjo","beekeeper","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buzzard","buzzing","buzzwords","cobweb","croquet","crypt","cycle","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","exodus","faking","fishhook","fixable","flapjack","flopping","fluffiness","flyby","frazzled","frizzled","funny","gabby","galaxy","galvanize","gazebo","gizmo","glowworm","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","icebox","injury","ivory","ivy","jackpot","jaundice","jaywalk","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","matrix","megahertz","microwave","mnemonic","mystify","nightclub","nowadays","numbskull","nymph","onyx","oxidize","oxygen","pajama","peekaboo","pixel","pneumonia","psyche","puppy","puzzling","quartz","queue","quips","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","twelfth","unknown","unworthy","unzip","uptown","vaporize","voodoo","vortex","walkway","waltz","wave","wavy","waxy","wheezy","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","xylophone","yacht","yippee","yoked","youthful","yummy","zigzag","zigzagging","zipper","zodiac","zombie"]
  with shelve.open('games') as db:
    if "games" in db:
      saved_games = db['games']
  crazy_games_string = ""
  # makes a super long string that deals with all of the information pertaining to class objects stored in saved_games
  for i in range(len(saved_games)):
    crazy_games_string += (str(i+1) + ".")
    crazy_games_string += "letters guessed:"
    for j in saved_games[i].guesses:
      crazy_games_string += str(j)
    crazy_games_string += ", "
    crazy_games_string += "Number of incorrect guesses:"
    crazy_games_string += str(saved_games[i].wrong)
    crazy_games_string += ", "
    crazy_games_string += "Word in progress:"
    for j in saved_games[i].random_word:
        if j in saved_games[i].guesses:
          crazy_games_string += str(j)
        else:
          crazy_games_string += str("_")
    crazy_games_string += "\n"
  crazy_games_string += str(len(saved_games) + 1) + ". start a new game!"
      
    
    
    
  
  if saved_games == []:
    print("No Games Available")
    global game
    game = Game(random.choice(words), [], 0)
    game.ascii()
    game.guess()
    
  else:
    global game_choice
    game_choice = int(input(crazy_games_string))
    if game_choice - 1 != len(saved_games):
      game = saved_games[game_choice - 1]
      game.ascii()
      game.guess()
    else:
      game = Game(random.choice(words), [], 0)
      game.ascii()
      game.guess()
    
  #atexit.register(save_object())
    
def start_menu():
  choice = int(input("Would you like to 1: log in or 2: make an account? "))
  ## Choice 1 causes log in function
  if choice == 1:
    username = str(input("Username: "))
    password = str(input("Password: "))
    Account.LogIn(username,password)
  ## Choice 2 causes create account function
  if choice == 2:
    username = str(input("Username: "))
    password = str(input("Password: "))
    Account.add_account(username, password)

start_menu()

# game.can_make_word(game.guesses)
