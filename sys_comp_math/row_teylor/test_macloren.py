import math
import unittest
import macloren as mac

class Tests_macloren(unittest.TestCase):

    def test_macloren_e(self):
        def test_macloren_e(self):
            n = 5
            x = 2
            answer = 7.266666666666667
            self.assertEqual(mac.macloren_e(n, x), answer)

    def test_macloren_cos(self):
        x = 4
        self.assertEqual(round(mac.macloren(x), 5), round(math.cos(4), 5))

    def test_macloren_sin(self):
        n = 5
        x = 1.5
        answer = 0.9974949556821353
        self.assertEqual(mac.macloren_sin(n, x), answer)


    def test_mac_arcsin(self):
        n = 3
        x = 1
        answer = 1.286309523809524
        self.assertEqual(mac.macloren_arcsin(n, x), answer)

    def test_mac_arccos(self):
        n = 2
        x = 1
        answer = 0.32912966012822986
        self.assertEqual(mac.macloren_arccos(n, x), answer)


if __name__ == '__main__':
    unittest.main()