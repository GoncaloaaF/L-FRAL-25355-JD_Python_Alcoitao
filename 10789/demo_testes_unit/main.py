import unittest

def soma(a:float, b:float) -> float:
    return a+b

class TestSoma(unittest.TestCase):

    def test_teste1(self):
        self.assertEqual(2,6)

    def test_teste2(self):
        self.assertEqual(32,6)

    def test_teste3(self):
        self.assertEqual(2,2)