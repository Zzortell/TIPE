#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments
from lib.XMLRepr import XMLRepr

from src.EvolutiveGenerator.GeneticElement import GeneticElement


class IA(GeneticElement, XMLRepr):
	"""An IA"""
	
	@inject_arguments
	def __init__(self, id, neurons=set()):
		"""Init the IA
		
		Expects:
			id to be a integer, unique among IA's of a processus
			neurons to be a set of Neuron
		"""
		
		pass
	
	
	def reprJSON(self):
		return self.__dict__
	
	def __repr__(self):
		return super().__repr__(displaySequencesNames=False)
