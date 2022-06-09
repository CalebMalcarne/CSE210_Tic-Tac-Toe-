
from Dice.die import Die

class diceGame:
   def __init__(self):

      self.dice = []
      self.playing = True

      for i in range(5):
         die = Die()
         self.dice.append(die)


   def getinput(self):
      inp = input("Rool dice [y/n]: ")
      if inp == 'y' or inp == 'Y':
         self.Playing = True
      elif inp == 'n':
         self.playing = False

   def startGame(self):
      while self.playing == True:
         self.getinput()
         self.outputs()

   def outputs(self):
      [self.dice[i].randNumber() for i in range(5)]
      nums = [self.dice[i].val for i in range(5)]
      print(nums)      

game = diceGame()
game.startGame()