from .item import *
import random

class Weapon(Item):
	def __init__(self, name, value, damage, quantity=1):
		Item.__init__(name, value, quantity)
		
		self.minDMG = damage[0]
		self.maxDMG = damage[1]

	def damage(self):
		return random.randint(self.minDMG, self.maxDMG)

class WeaponEnchanted(Weapon):
	def __init__(self, name, value, damage, effects, quantity=1):
		Weapon.__init__(name, value, quantity)

		self.effects = effects

items = [
	Weapon("Longsword", 25, (7, 12)),
	Weapon("Greatsword", 50, (5, 14))
]

for item in items:
	print(item.damage())
