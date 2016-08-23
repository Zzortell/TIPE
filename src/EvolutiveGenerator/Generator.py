#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import choice, sample
from math import ceil


class Generator:
	"""Handle the generation proccess
	
	The generator, at the heart of the generation process, has three charges:
		- create a population of individuals
		- operate the selection, based on individuals' performances
		- generate a new population, based on the selection
	Individuals are represented by root GeneticElement instances.
	Use a Graduator to grade performances.
	Extending it is strongly adviced.
	"""
	
	
	def __init__(self, factory, graduator):
		"""Init
		
		Expects:
			factory to be a class inheriting of GeneticElementFactory
			graduator to be a instance inheriting of Graduator
		"""
		
		self.factory = factory
		self.graduator = graduator
		self.population = None
		self.selection = None
		self.generation = 0
	
	
	def create(self, length):
		"""Generate a whole initial population"""
		
		self.population = set([self.factory.create() for i in range(length)])
		
		# print('------------------------------------------------------------')
		# print(self.population)
		# print('------------------------------------------------------------')
	
	
	def select(self, proportion, chance):
		"""Operate the selection
		
		This is a basic system to be overcome.
		The selection is a subset of the population.
		
		Expects:
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		"""
		
		# Get a list of couple (score, individual) sorted by score
		graded_individuals = self.graduator.gradeAll(self.population, self.generation)
		# Get a list of individuals
		ordered_individuals = [c[1] for c in graded_individuals]
		
		# The number of individuals to select
		number = ceil(len(self.population) * proportion)
		# Among the [number] best individuals select number*(1-chance) ones
		selection = set(sample(
			ordered_individuals[:number],
			int(number*(1-chance))
		))
		# Complete selection with random individuals
		unused_individuals = self.population.difference(selection)
		while len(selection) < number:
			choiced = choice(unused_individuals)
			selection.add(choiced)
			unused_individuals.remove(choiced)
		
		self.selection = selection
	
	
	def generate(self, length):
		"""Generate a new population based on selection
		
		This is a basic system to be overcome.
		"""
		
		new_pop = set()
		
		while len(new_pop) < length:
			parents = tuple([choice(list(self.selection)) for i in range(2)])
			new_pop.add(self.factory.generate(*parents))
		self.population = new_pop
	
	
	def run(self, length, proportion, chance):
		"""Operate a run"""
		
		self.select(proportion, chance)
		self.generate(length)
		self.generation += 1
	
	
	def process(self, number, length = 500, proportion = .5, chance = 0):
		"""Process multiple runs
		
		Expects:
			number to be an int
			length to be an int
			
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		
		Return the last generation
		"""
		
		self.create(length)
		self.generation = 1
		
		for i in range(number):
			self.run(length, proportion, chance)
		
		return self.population
