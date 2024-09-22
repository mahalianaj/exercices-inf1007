#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	first_name = name.split("-")[0]
	final = first_name.upper()[0] + first_name.lower()[1:]
	return "Bonjour, " + final

	#first_name = first_name.lower()
	#for letter in first_name:
		#if letter[0].islower():
			#letter = letter[0].upper()
			#break
	#final = letter[0] + first_name[1:]
	
	
	

def get_random_sentence(animals, adjectives, fruits):
	animals = random.choice(animals)
	adjectives = random.choice(adjectives)
	fruits = random.choice(fruits)

	return "Aujourd’hui, j’ai vu un " + animals + " s’emparer d’un panier " + adjectives + " plein de " + fruits 
	#animal = animals[ramdom.randrange(len(animals))]
	#adjectives = adjectives[ramdom.randrange(len(adjectives))]
	#fruits = fruits[ramdom.randrange(len(fruits))]


def format_date(year, month, day, hours, minutes, seconds):
	#date = f"{year[:4]}-{day[:2]}-{month[:2]}  {hours[:2]}:{minutes[:2]}:{seconds:06.3f}"
	return 

def encrypt(text, shift):
	result = ""
	for letter in text: 
		encrypted_text = letter
		if letter.isalpha():
			index = ord(letter.upper())-ord("A")
			encrypted_index = (index+shift) %26
			encrypted_letter = chr(ord("A")) + encrypted_index
		result += encrypted_letter
	return result
	

	

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
