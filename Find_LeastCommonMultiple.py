#!/usr/bin/env python
#coding: utf8

"""1. На основе существующей функции нахождения НОД, напишите функцию поиска НОК двух чисел.
	def gcd(a, b):
   "Нахождение НОД"
   while a != 0:
      a,b = b%a,a # параллельное определение
   return b """

def lcm(a,b):
	"""Нахождение НОК 
	(Наименьшее общее кратное для нескольких чисел — это наименьшее натуральное число, 
	 которое делится на каждое из этих чисел)"""
	
	# parameters for НОД (наибольший общий делитель)
	k1 = a
	k2 = b
	while k1 != 0:
		k1,k2 = k2%k1,k1 # параллельное определение

	flcm = abs(a*b)/k2
	return flcm