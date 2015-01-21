
# Main game file

import textwrap
from Characters.player import *
from Commands.commands import *
from Utilities.util import *
from Items.item import *
from Locations.room import *
from test import *

def start():
	print ""
	print ""
	print "     Welcome To       "
	print "            _   _     "
	print " /\ /\ _ __| |_| |__  "
	print "/ / \ \ '__| __| '_ \ "
	print "\ \_/ / |  | |_| | | |"
	print " \___/|_|   \__|_| |_|"
        print ""
	print "(Created by: Illyduss)"
	print ""
	print ""

def help(player,args):
	for command in commands:
		print(command)

commands = {
	'help': help,
	'quit': exit,
	'inv': inv,
	'look': look
}

player = Player("Default", 1, 1, 1, 1)

def nameInput(prompt):
	name = raw_input(prompt)
	return name.strip()

def getName():
	tempName = ""
	while 1:
		tempName = nameInput("What is your name? ")

		if len(tempName) < 1:
			continue

		yes = yesOrNo(tempName.capitalize() + ", is that your name? ")

		if yes:
			return tempName
		else:
			continue

def isValidCMD(cmd):
	if cmd in commands:
		return True
	return False

def runCMD(cmd, args, player):
	commands[cmd](player, args)

def main(player):

	player.name = getName()
	player.loc = getRoom(1)

	while (not player.dead):
		line = raw_input(">> ")
		input = line.split()
		input.append("EOI")
		
		if isValidCMD(input[0]):
			runCMD(input[0], input[1], player)

start()
main(player)
