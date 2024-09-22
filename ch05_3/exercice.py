#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
	sum=0
	for elem in text:
		if elem.isalnum():
			sum+=1
	return sum

def get_word_length_histogram(text):
	mots = text.split()
	hist = []
	
	max_let = max(mots)
	for word in range(mots, max_let):
		count = 0 
		for letter in word:
			count += 1
			hist.append(count)


	return [0]

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
