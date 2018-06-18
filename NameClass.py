#-*- coding: utf-8 -*-

#NameClass
#l_NameClass
#argv_NameClass
#nameclassHelp
#nameclass
#menu_NameClass
#menu_NameClass_for_LuPa
#init_NameClass
#show_menu_NameClass

from sys import argv
from os import system

class NameClass():
	l_NameClass = 0
	argv_NameClass = []

	def __init__(self, argv_a):
		self.l_NameClass = len(argv_a)
		self.argv_NameClass = argv_a

	def showTitle(self):
		print("### \"Name Class\" (NameClass) (random) 1.0.0   ###")
		print("###      by Name (c) 1970  	                 ###")

	def point_0(self):
		pass

	def point_1(self):
		pass

	def point_2(self):
		pass

	def nameclassHelp(self):
		print("""
* NameClass v0.0 by Name (c) 1070 *

-----------

nameclass []
    	  []
          []

--------------------
--------------------

nameclass -n    -----------------------------

nameclass -s    -----------------------------
		""")

	def enter_number(self):
		print("Enter number or press <ENTER> for default.")
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

	def nameclass(self, plus = 0):
		if self.l_NameClass == 1+plus:
			pass
			#------
		elif self.l_NameClass == 2+plus:
			if self.argv_NameClass[1+plus] == "-h":
				self.nameclassHelp()
			else:
				print('[', self.argv_NameClass[1+plus], "] - not find argument.")

	def menu_NameClass(self, index = 0):
		print("NameClass ()")
		print(index, "  Point 0")
		print(index+1, "  Point 1")
		print(index+2, "  Point 2")
		return index+2

	def menu_NameClass_for_LuPa(self, index = 99):
		num = 0
		if index == 99:
			menu_NameClass()
		else:
			num = self.enter_number()
			print()

		if index == 0:
			pass
			#point 0
		elif index == 1:
			pass
			#point 1
		elif index == 2:
			pass
			#point 2

			
def init_NameClass(argv_a):
	NameClass(argv_a).nameclass(1)

def show_menu_NameClass(index):
	return NameClass([]).menu_NameClass(index)

def menu_NameClass(index):
	NameClass([]).menu_NameClass_for_LuPa(index)

def main():
	N = NameClass(argv)

	if len(argv) == 1:
		pass
		#Menu NameClass
	else:
		N.nameclass()

if __name__ == '__main__':
	main()


