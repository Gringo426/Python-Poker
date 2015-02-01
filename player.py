import copy

class Player:
	def __init__(self, name, money):
		self.name = name
		self.money = float(money)
		self.hand = []

	def getMoney(self):
		return self.money

	def getName(self):
		return self.name

	def getHand(self):
		self.hand.sort()
		return self.hand

	def addToHand(self, card):
		self.hand.append(card)

	def resetHand(self):
		self.hand = []

	def removeCard(self, position):
		self.hand.pop(position)
		return

	def getHandValue(self):
		hVL = []
		for card in self.hand:
			hVL.append(card[0])
		hVS = list(set(hVL))
		hVS.sort()
		if len(hVS) == 2:
			for x in range(len(hVS)):
				if hVL.count(hVS[x]) == 4:
					return 7+float(hVS[x])/100 # Four of a kind with sorting by value
				elif hVL.count(hVS[x]) == 3:
					return 6+float(hVS[x])/100 # Full House
		elif len(hVS) == 3:
			for y in range(len(hVS)):
				if hVL.count(hVS[y]) == 3:
					return 3+float(hVS[y])/100 # Three of a kind with sorting by value
			return 2 # Two Pair
		elif len(hVS) == 4:
			for x in range(len(hVS)):
				if hVL.count(hVS[x]) == 2:
					return 1+float(hVS[x])/100 # One Pair with sorting by value
		elif self.straight() > -1:
			if self.flush() > -1:
				return 8+flot(hVS[len(hVS)-1])/100 # Straight Flush
			else:
				return 4+float(hVS[len(hVS)-1])/100 # Straight
		elif self.flush() > -1:
			return 5+float(hVS[len(hVS)-1])/100 # Flush
		else:
			return 0+float(hVS[len(hVS)-1])/100


	def straight(self):
		startHand = []
		lHand = []
		aHand = []
		finalHand = []
		straightProb = 1
		for card in self.hand:
			startHand.append(card[0])
		lHand = list(set(startHand))
		lHand.sort()
			
		for y in range(len(lHand)-1):
			if lHand[y]+1 == lHand[y+1]:
				aHand.append(lHand[y])
				aHand.append(lHand[y+1])
			else:
				aHand = []

			if len(aHand) >= 6:
				finalHand = copy.deepcopy(aHand)

		finalHand = list(set(finalHand))

		if len(finalHand) == 5:
			return 4+float(finalHand[len(finalHand)-1])/100 # Straight
		else:
			return -1 # Not Straight


	def flush(self):
		handSuit = []
		suitCount = []
		suitList = ["C", "D", "H", "S"]
		cardValue = []
		for card in self.hand:
			handSuit.append(card[1])
			cardValue.append(card[0])
		cardValue.sort()
		if len(set(handSuit)) == 1:
			return 5+float(cardValue[len(cardValue)-1]/100) # Flush
		else:
			return -1 # Not Flush

	def testHand(self, cards):
		self.hand = copy.deepcopy(cards)
