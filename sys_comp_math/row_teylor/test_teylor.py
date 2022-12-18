import math
import unittest
import teylor as tey


class Tests_teylor(unittest.TestCase):

    def test_teylor_e(self):
        x = 3
        self.assertEqual(round(tey.teylor_e(x), 5), round(math.exp(x), 5))

    def test_teylor_cos(self):
        x = 4
        self.assertEqual(round(tey.teylor_cos(x), 5), round(math.cos(4), 5))

    def test_teylor_sin(self):
        x = 4
        self.assertEqual(round(tey.teylor_sin(x), 5), round(math.sin(4), 5))

    # def test_teylor_sin(self):
    #     x = 4
    #     self.assertEqual(round(tey.teylor_arcsin(x), 5), round(math.asin(x), 5))

print(tey.teylor_arcsin(1))
print(math.sin(1))

if __name__ == '__main__':
    unittest.main()