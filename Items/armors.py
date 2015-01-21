from .item import *

class Armor(Item):
	def __init__(self, name, value, defense, quantity=1)
		Item.__init__(name, value, quantity)

		self.defense = defense
