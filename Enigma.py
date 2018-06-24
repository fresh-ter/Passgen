#-*- coding: utf-8 -*-

#Enigma
#l_Enigma
#argv_Enigma
#enigmaHelp
#enigma
#menu_Enigma
#menu_Enigma_for_LuPa
#init_Enigma
#show_menu_Enigma

from sys import argv
from os import system

class Enigma():
	l_Enigma = 0
	argv_Enigma = []

	def __init__(self, argv_a):
		self.l_Enigma = len(argv_a)
		self.argv_Enigma = argv_a

	def showTitle(self):
		print("### \"Encoder and decoder\" (Enigma) (random) 1.0.0   ###")
		print("###      by Fresh Perspective (c) 2018  	                 ###")

	def abc_encode(self):
		string = self.get_string()

		abc = [	'а', 'б', 'в', 'г', 'д', 'е', 'ё',
		'ж', 'з', 'и', 'й', 'к', 'л', 'м',
		'н', 'о', 'п', 'р', 'с', 'т', 'у',
		'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
		'ы', 'ь', 'э', 'ю', 'я' ]

		s1 = ''
		s = str(string)

		for number1 in range(int(len(s))):
			for number in range(int(len(abc))):
				if s[number1] == abc[number]:
					s1 += str(number+1)
					s1 += ","
					break
				elif s[number1] == " ":
					s1 += " "
					break
		return s1

	def abc_decode(self):
		string = self.get_string()

		abc = [	'а', 'б', 'в', 'г', 'д', 'е', 'ё',
		'ж', 'з', 'и', 'й', 'к', 'л', 'м',
		'н', 'о', 'п', 'р', 'с', 'т', 'у',
		'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
		'ы', 'ь', 'э', 'ю', 'я' ]

		s1 = ''
		s = str(string)

		s2 = ''

		for number1 in range(int(len(s))):
			if s[number1] != "," and s[number1] != " ":
				s2 += s[number1]
			elif s[number1] == ",":
				for number in range(int(len(abc))):
					if int(s2)-1 == number:
						s1 += str(abc[number])
						break
				s2 = ""
			elif s[number1] == " ":
				s1 += " "
		return s1

	def point_1(self):
		pass

	def point_2(self):
		pass

	def get_string(self):
		print("Enter string for en- de- coder or press <ENTER> for default.")
		print("(Default = 'Hello world!')")
		s = ''
		try:
			s = str(input('~'))
		except ValueError:
			s = 'Hello world!'
		except EOFError:
				system("cls")
				exit()
		return s

	def enigmaHelp(self):
		print("""
* Enigma v1.0 by Fresh Perspective (c) 2018 *

Encoding and decoding

enigma  [-abc string]
    	[-abc -d string]

By default incode and decode string "Hello world!".

enigma -abc  Encoding string according
		  to the number of chars in the alphabet
		""")

	def enigma(self, plus = 0):
		if self.l_Enigma == 1+plus:
			pass
			#------
		elif self.l_Enigma == 2+plus:
			if self.argv_Enigma[1+plus] == "-h": # enigma -h
				self.enigmaHelp()
			elif self.argv_Enigma[1+plus] == "-abc": # enigma -abc
				print(self.abc_encode())
			else:
				print('[', self.argv_Enigma[1+plus], "] - not find argument.")
		elif self.l_Enigma == 3+plus:
			if self.argv_Enigma[1+plus] == "-abc": # enigma -abc
				if self.argv_Enigma[2+plus] == "-d":
					print(self.abc_decode())

	def menu_Enigma(self, index = 0):
		print("Enigma (Encoder and decoder)")
		print(index, "  ABC encoder")
		print(index+1, "  ABC decoder")
		return index+1

	def menu_Enigma_for_LuPa(self, index = 99):
		num = 0
		if index == 99:
			menu_Enigma()

		if index == 0:
			print(self.abc_encode())
		elif index == 1:
			print(self.abc_decode())
		

			
def init_Enigma(argv_a):
	Enigma(argv_a).enigma(1)

def show_menu_Enigma(index):
	return Enigma([]).menu_Enigma(index)

def menu_Enigma(index):
	Enigma([]).menu_Enigma_for_LuPa(index)

def main():
	N = Enigma(argv)

	if len(argv) == 1:
		system("cls")

		s=0

		N.showTitle()
		print()
		N.menu_Enigma()

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
		
		N.menu_Enigma_for_LuPa(s)	
	else:
		N.enigma()

if __name__ == '__main__':
	main()


