from deck import Deck
from player import Player
import copy

class Game:
	def __init__(self, arguments):
		try:
			if arguments[1] == "--suppress":
				self.suppressErr = True
			else:
				self.suppressErr = False
		except:
			self.suppressErr = False
		self.deck = Deck()
		self.players = []
		self.handSize = 5
		# Multiple Redraws not implemented yet
		self.totalRedraws = 1


	def addPlayer(self, name, money):
		if ((len(self.players)+1)*self.handSize*(self.totalRedraws+1)) > self.deck.deckSize:
			if not self.suppressErr:
				print("Cannot add player " + str(name) + ".")
			return
		newPlayer = Player(name, money)
		self.players.append(newPlayer)


	def deal(self):
		if len(self.players)*self.handSize > self.deck.size():
			self.deck.reset()
		for pl in self.players:
			pl.resetHand()
		for x in range(self.handSize):
			for pl in self.players:
				self.deck.dealOne(pl)


	def getNewHand(self):
		cardsToDrop = ""
		for pl in self.players:
			hand = pl.getHand()
			output = ""
			output+= pl.getName() + ": "
			for x in hand:
				output+= str(x[0]) + x[1] + " "
			print(output)
			cont = False
			while not cont:
				cont = True
				cardsToDrop = input("Enter the position of the cards you would like to redraw. ")
				cardsToDrop = cardsToDrop.split(" ")
				if cardsToDrop[0] == "":
					break
				for x in cardsToDrop:
					if int(x) > self.handSize or int(x) < 1:
						print("Invalid input.\n" + output + " ")
						cont = False
						break
			count = 0
			if cardsToDrop[0] == "":
				pass
			else:
				for x in cardsToDrop:
					pl.removeCard(int(x)-1-count)
					count+=1
				cardsToDeal = self.handSize - len(pl.getHand())
				for x in range(cardsToDeal):
					self.deck.dealOne(pl)


	def findWinner(self):
		handValues = []
		sHandValues = []
		for pl in self.players:
			handValues.append([pl.getHandValue(), pl.getName(), pl.getHand()])

		handValues.sort(reverse=True)

		for x in handValues:
			sHandValues.append([x[1], x[2], x[0]])

		for x in sHandValues:
			output = str(x[0]) + "\t"
			for y in x[1]:
				output += str(y[0]) + str(y[1]) + " "
			output += "   \t" + str(x[2])
			print(output)
