import copy
import random

class Deck:
	def __init__(self):
		tempA = []
		self.usedCards = []
		self.suitList = ["C", "D", "H", "S"]
		for x in range(2,15):
			for y in self.suitList:
				tempC = [x, y]
				tempA.append(tempC)
		self.defaultDeck = [tempA, len(tempA)]
		self.currentDeck = copy.deepcopy(self.defaultDeck[0])
		self.deckSize = copy.deepcopy(self.defaultDeck[1])

	def reset(self):
		self.currentDeck = copy.deepcopy(self.defaultDeck[0])
		self.deckSize = copy.deepcopy(self.defaultDeck[1])
		self.usedDeck = []

	def dealOne(self, player):
		cN = random.randint(0, self.deckSize-1)
		rV = self.currentDeck[cN]
		self.usedCards.append(rV)
		self.currentDeck.pop(cN)
		self.deckSize -= 1
		player.addToHand(rV)
		return


	def size(self):
		return self.deckSize
