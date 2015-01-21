
import sys

def exit(player, args):
	sys.exit("Thank you for playing!")

def inv(player, args):
	for item in player.inventory:
		print("{0} x{1}".format(item.name, item.quantity))

def move(player, dir):
	newroom = player.connect(dir)
	if newroom is None:
		print("You cannot go that way.")
	else:
		player.loc = getRoom(newroom)
		player.look()

def look(player, args):
	print(player.loc.name)
	print("")
	print (player.loc.description)

def do_n(self, args):
	"""Move north"""
	self.move('n')

def do_ne(self, args):
	"""Move northeast"""
	self.move('ne')

def do_e(self, args):
	"""Move east"""
	self.move('e')

def do_se(self, args):
	"""Move southeast"""
	self.move('se')

def do_s(self, args):
	"""Move south"""
	self.move('s')

def do_sw(self, args):
	"""Move southwest"""
	self.move('sw')

def do_w(self, args):
	"""Move west"""
	self.move('w')

def do_nw(self, args):
	"""Move northwest"""
	self.move('nw')

def do_u(self, args):
	"""Move up"""
	self.move('u')

def do_d(self, args):
	"""Move down"""
	self.move('d')
