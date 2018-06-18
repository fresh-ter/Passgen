#-*- coding: utf-8 -*-
import random
from sys import argv
from os import system

number_Menu = 0

class Passgen():
	l_Passgen = 0
	argv_Passgen = []

	def __init__(self, argv_a):
		self.l_Passgen = len(argv_a)
		self.argv_Passgen = argv_a

	def showTitle(self):
		print("### \"Passwort generator\" (Passgen) (random) 1.0.0   ###")
		print("###      by Fresh Perspective (c) 2018      	    ###")

	def passw_generator_random(self, count_char = 8):
		arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
		'K', 'I', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
		'V', 'W', 'X', 'Y', 'Z',
			   '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		passw = []

		for i in range(count_char):
			passw.append(random.choice(arr))

		return "".join(passw)

	def passw_N_generator_random(self, count_char = 8):
		arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		passw = []

		for i in range(count_char):
			passw.append(random.choice(arr))

		return "".join(passw)

	def passw_S_generator_random(self, count_char = 8):
		arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
		'K', 'I', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
		'V', 'W', 'X', 'Y', 'Z']
		passw = []

		for i in range(count_char):
			passw.append(random.choice(arr))

		return "".join(passw)

	def passgenHelp(self):
		print("""
* Passgen v1.0 by Fresh-Perspective (c) 2018 *

Creating random password

passgen [number_chars]
    	[-s | -s number_letters]
    	[-n | -n number_digits]
        [-h]

By default creates password of 8 chars.
(In the password will are present letters and digits)

passgen -n    Creating password of 8 chars.
		  In the password will are present only digits.

passgen -s    Creating password of 8 chars.
	      In the password will are present only letters.
		""")

	def enter_number(self):
		print("Enter number chars in password or press <ENTER> for default.")
		print("(Default = 8)")
		s = 0
		try:
			s = int(input('~'))
		except ValueError:
			s = 8
		except EOFError:
				system("cls")
				exit()
		return s

	def passgen(self, plus = 0):
		if self.l_Passgen == 1+plus:
			print(self.passw_generator_random())
		elif self.l_Passgen == 2+plus:
			if self.argv_Passgen[1+plus] == "-n":
				print(self.passw_N_generator_random())
			elif self.argv_Passgen[1+plus] == "-s":
				print(self.passw_S_generator_random())
			elif self.argv_Passgen[1+plus] == "-h":
				self.passgenHelp()
			else:
				try:
					number = int(self.argv_Passgen[1+plus])
					print(self.passw_generator_random(number))
				except ValueError:
					print('[', self.argv_Passgen[1+plus], "] - not find argument.")
		elif self.l_Passgen == 3+plus:
			number = 0
			try:
				number = int(self.argv_Passgen[2+plus])
			except ValueError:
				print('[', self.argv_Passgen[2+plus], "] - not number.")

			if self.argv_Passgen[1+plus] == "-n":
				print(self.passw_N_generator_random(number))
			elif self.argv_Passgen[1+plus] == "-s":
				print(self.passw_S_generator_random(number))
			elif self.argv_Passgen[1+plus] == "-h":
				self.passgenHelp()
			else:
				print('[', self.argv_Passgen[1+plus], "] - not found argument.")

	def menu_Passgen(self, index = 0):
		print("Passgen (Password generator random)")
		print(index, "  Password of digits and letters")
		print(index+1, "  Password of only digits")
		print(index+2, "  Password of only letters")
		return index+2

	def menu_Passgen_for_LuPa(self, index = 99):
		num = 0
		if index == 99:
			menu_Passgen()
		else:
			num = self.enter_number()
			print()

		if index == 0:
			print(self.passw_generator_random(num))
		elif index == 1:
			print(self.passw_N_generator_random(num))
		elif index == 2:
			print(self.passw_S_generator_random(num))

			
def init_Passgen(argv_a):
	#print("argv_a =", argv_a)

	Passgen(argv_a).passgen(1)

def show_menu_Passgen(index):
	return Passgen([]).menu_Passgen(index)

def menu_Passgen(index):
	Passgen([]).menu_Passgen_for_LuPa(index)

def main():
	P = Passgen(argv)

	if len(argv) == 1:
		system("cls")

		P.showTitle()
		print()
		P.menu_Passgen()

		s = 0

		while True:
			try:
				s = int(input('~'))
				break
			except ValueError:
				print("You entered the wrong data!")
			except EOFError:
					system("cls")
					exit()
		print()
		
		P.menu_Passgen_for_LuPa(s)	
	else:
		P.passgen()

if __name__ == '__main__':
	main()


