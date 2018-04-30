import Measures
import unittest

class TestMeasures:
	def test_degree(self,g):
		e=self.g.size()
		fun=Node()
		deg=len(fun.degree_dist(self,g))
		assert e==deg
