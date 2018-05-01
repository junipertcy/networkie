import unittest
import networkx as nx

import machine
from Custom import LoadFromFile

g = LoadFromFile()
G = g.from_in_class_network('In-class_network.txt')

class MachineTest(unittest.TestCase):
	def setUp(self):
		self.args = G

	def tearDown(self):
		self.args = None

	def test_degree_dist(self):
		expected = 2 * len(list(self.args.edges()))
		result = sum(machine.degree_dist(self.args))

		self.assertEqual(expected, result)

#python -m pytest test_compute_degrees.py