#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Optional

from pynput import keyboard
from pynput.keyboard import Key

from random import choice
import numpy as np

# TODO:
# - move every functions related to interpretation / execution to llm.py

class LabyrintheParfait:
	'''
	'''
	def __init__(self, L: int, l: int) -> None:
		
		self.L, self.l = L, l

		self.cases, self.cases_visitees = L * l, 1
		self.case_courante = choice(range(self.cases))
		self.nouvelle_case = self.case_courante

		self.marche_arriere = False
		self.mouvements = [-L, -1, 1, L]
		self.chemin = [-1] * self.cases
		self.chemin[self.case_courante] = self.case_courante

		# Le labyrinthe
		self.labyrinthe = np.chararray((2 * l + 1, 2 * L + 1), unicode = True)
		self.labyrinthe.fill('-')

		# Bords
		self.labyrinthe[0, :] = self.labyrinthe[-1, :] = self.labyrinthe[:, 0] = self.labyrinthe[:, -1] = '#'

	def dessiner_labyrinthe(self) -> None:
		'''
		'''
		print('\n'.join(map(''.join, self.labyrinthe)))

	def choisir_case(self) -> None:
			'''
			'''
			liste_cases = []
			for direction in self.mouvements:
				self.nouvelle_case = self.case_courante + direction
				if 0 <= self.nouvelle_case < self.cases:
					if self.nouvelle_case % self.L == self.case_courante % self.L or self.nouvelle_case // self.L == self.case_courante // self.L:
						if self.chemin[self.nouvelle_case] == -1:
							liste_cases.append(self.nouvelle_case)
						elif self.nouvelle_case != self.chemin[self.case_courante] and not self.marche_arriere:
							x, y = self.case_courante // self.L, self.case_courante % self.L
							if direction == -self.L:
								self.labyrinthe[2 * x, 2 * y : 2 * y + 3] = '#'
							elif direction == self.L:
								self.labyrinthe[2 * x + 2, 2 * y : 2 * y + 3] = '#'
							elif direction == -1:
								self.labyrinthe[2 * x : 2 * x + 3, 2 * y] = '#'
							else:
								self.labyrinthe[2 * x : 2 * x + 3, 2 * y + 2] = '#'
			if liste_cases == []:
				self.marche_arriere = True
			else:
				self.nouvelle_case = choice(liste_cases)
				self.marche_arriere = False

	def creer_labyrinthe(self) -> None:
		'''
		'''
		while self.cases_visitees < self.cases:
			self.choisir_case()

			if not self.marche_arriere:
				self.chemin[self.nouvelle_case] = self.case_courante
				self.case_courante = self.nouvelle_case
				self.cases_visitees += 1
			else:
				self.case_courante = self.chemin[self.case_courante]
		self.choisir_case()

l, L = 10, 20
lab = LabyrintheParfait(L, l)
lab.creer_labyrinthe()

joueur = '@'
# Placement du joueur:
x, y = 0, 0
while lab.labyrinthe[x, y] != '-':
	x, y = np.random.randint(1, 2 * l + 1), np.random.randint(1, 2 * L + 1)

lab.labyrinthe[x, y] = joueur

# def on_key_release(key):
	# global x, y

	# X, Y = x, y
	# if key == Key.right:
		# Y += 1
	# elif key == Key.left:
		# Y -= 1
	# elif key == Key.up:
		# X -= 1
	# elif key == Key.down:
		# X += 1
	# elif key == Key.esc:
		# return False

	# if lab.labyrinthe[X, Y] == '-':
		# lab.labyrinthe[x, y] = '-'
		# lab.labyrinthe[X, Y] = '@'
		# x, y = X, Y

	# print()
	# lab.dessiner_labyrinthe()

# with keyboard.Listener(on_release = on_key_release) as listener:
	# listener.join()

def label(name: str) -> tuple[int, int]:
	match name:
		case "A":
			return A
		case _:
			raise(ValueError("Invalid label name: " + name))

def point(x: int, y: int) -> tuple[int, int]:
	return x, y

def right(n: Optional[int] = float('inf')) -> None:
	global x, y

	i = 1
	while (i <= n) and (lab.labyrinthe[x, y + i] == '-'):
		i += 1
	if lab.labyrinthe[x, y + i - 1] == '-':
		lab.labyrinthe[x, y] = '-'
		lab.labyrinthe[x, y + i - 1] = '@'
		y += i - 1

def left(n: Optional[int] = float('inf')) -> None:
	global x, y

	i = 1
	while (i <= n) and (lab.labyrinthe[x, y - i] == '-'):
		i += 1
	if lab.labyrinthe[x, y - i + 1] == '-':
		lab.labyrinthe[x, y] = '-'
		lab.labyrinthe[x, y - i + 1] = '@'
		y -= i - 1


def up(n: Optional[int] = float('inf')) -> None:
	global x, y

	i = 1
	while (i <= n) and (lab.labyrinthe[x - i, y] == '-'):
		i += 1
	if lab.labyrinthe[x - i + 1, y] == '-':
		lab.labyrinthe[x, y] = '-'
		lab.labyrinthe[x - i + 1, y] = '@'
		x -= i - 1


def down(n: Optional[int] = float('inf')) -> None:
	global x, y

	i = 1
	while (i <= n) and (lab.labyrinthe[x + i, y] == '-'):
		i += 1
	if lab.labyrinthe[x + i - 1, y] == '-':
		lab.labyrinthe[x, y] = '-'
		lab.labyrinthe[x + i - 1, y] = '@'
		x += i - 1


