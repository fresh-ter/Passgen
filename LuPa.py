#-*- coding: utf-8 -*-
import random
from sys import argv
from os import system
from getpass import getpass



from Passgen import init_Passgen, show_menu_Passgen, menu_Passgen

menu_Passgen_begin = 0
menu_Passgen_end = 0

from Enigma import init_Enigma, show_menu_Enigma, menu_Enigma

menu_Enigma_begin = 0
menu_Enigma_end = 0



LOGIN = "root"
PASSWORD = "root"

l = len(argv)


def showTitle():
	print("###           Utility Manager           ###")
	print("### \"Login und Passwort\" (LuPa) 1.0.0   ###")
	print("###     by Fresh Perspective (c) 2018   ###")


def menu_lupa_start():
	showTitle()

	print()
	print("~~~~~~~~~~~~UTILITY~~~~~~~~~~~~")
	print()
	
	menu_Passgen_begin = index
	index = show_menu_Passgen(index)
	menu_Passgen_end = index

	menu_Enigma_begin = index
	index = show_menu_Enigma(index)
	menu_Enigma_end = index

	print()
	print("LuPa")
	print("99  Exit")
	print()

def menu_lupa_loop():
	showTitle()

	print()
	print("~~~~~~~~~~~~UTILITY~~~~~~~~~~~~")
	print()

	print(menu_Passgen_begin)
	print(menu_Enigma_begin)
	
	show_menu_Passgen(menu_Passgen_begin)
	
	show_menu_Enigma(menu_Enigma_begin)
	
	print()
	print("LuPa")
	print("99  Exit")
	print()

def menu_LuPa():
	global menu_Passgen_begin
	global menu_Passgen_end
	global menu_Enigma_begin
	global menu_Enigma_end

	number = 0
	ind = 0
	index = 0

	system('cls')

	while True:
		if ind == 0:
			showTitle()

			print()
			print("~~~~~~~~~~~~UTILITY~~~~~~~~~~~~")
			print()

			menu_Passgen_begin = index
			index = show_menu_Passgen(index)
			menu_Passgen_end = index

			index += 1

			menu_Enigma_begin = index
			index = show_menu_Enigma(index)
			menu_Enigma_end = index

			print()
			print("LuPa")
			print("99  Exit")
			print()
			ind = 1
		else:
			menu_lupa_loop()
		while True:
			try:
				number = int(input('Enter number:'))
				break
			except ValueError:
				print("You entered the wrong data!")
			except EOFError:
				system("cls")
				exit()

		print(menu_Passgen_begin)
		print(menu_Passgen_end)
		print(menu_Enigma_begin)
		print(menu_Enigma_end)
		if number == 99:
			system("cls")
			exit()


		elif number >= menu_Passgen_begin and number <=menu_Passgen_end:
			menu_Passgen(number - menu_Passgen_begin)
		elif number >= menu_Enigma_begin and number <=menu_Enigma_end:
			menu_Enigma(number - menu_Enigma_begin)


		print()
		print()
		print()
		system("pause")
		system("cls")



def login():
	i = 0

	while i < 4:
		l = str(input("login: "))
		p = str(getpass("password: "))

		if l == LOGIN:
			if p == PASSWORD:
				return 1234
		print("Incorrect username or password.")
		i =+ 1

	print("Authorization completed unsuccessfully!")
	exit()

def arguments_cmd():
	if argv[1] == 'passgen':
		init_Passgen(argv)
	elif argv[1] == 'enigma':
		init_Enigma(argv)
	else:
		print('[', argv[1], "] - not found utility.")

def main():
	# if login() == 1234:

	if l == 1:
		menu_LuPa()
	else:
		arguments_cmd()

if __name__ == "__main__":
	main()