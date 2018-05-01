import unittest
import hw3

ki = sum(hw3.k)
e = hw3.G.size()

class TestStringMethods(unittest.TestCase):

	def test_e(self):
		self.assertEqual( e , hw3.G.size() )
	
	def test_ee(self):
		self.assertTrue( e == ki/2 )
		self.assertFalse( e != ki/2)

if __name__ == '__main__':
	unittest.main()