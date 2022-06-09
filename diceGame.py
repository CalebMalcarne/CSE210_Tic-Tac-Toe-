
from Dice.die import Die

class diceGame:
   def __init__(self):

      self.dice = []
      self.playing = True
      self.score = 0

      for i in range(5):
         die = Die()
         self.dice.append(die)

   def updateScore(self):
      [self.dice[i].randNumber() for i in range(5)]
      for i in range(5):
         self.score += self.dice[i].points
      #[self.score + self.dice[i].points for i in range(5)]

   def getinput(self):
      inp = input("Rool dice? [y/n]: ")
      if inp == 'y' or inp == 'Y':
         self.Playing = True
      elif inp == 'n':
         self.playing = False

   def startGame(self):
      while self.playing == True:
         self.getinput()
         self.updateScore()
         self.outputs()

   def outputs(self):
      val = ""
      a = [self.dice[i].val for i in range(5)]

      for i in a:
         val += f"{i} "
      print(val)
      print(self.score)
      if 5 not in a and 1 not in a:
         self.playing = False
         

game = diceGame()
game.startGame()