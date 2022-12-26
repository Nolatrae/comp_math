import math
import unittest
import macloren as mac

class TestsMacloren(unittest.TestCase):


    def test_macloren_e(self):
        x = 1
        n = 3
        answer = 2.667
        self.assertEqual(round(mac.macloren_e(x, n), 3), answer)



    def test_macloren_cos(self):
        x = 5
        n = 5
        answer = -0.163
        self.assertEqual(round(mac.macloren_cos(x, n), 3), answer)

    def test_macloren_sin(self):
        x = 1
        n = 2
        answer = 0.8416666666666667
        self.assertEqual(mac.macloren_sin(x, n), answer)


    def test_mac_arcsin(self):
        x = 1
        n = 3
        answer = 0.179
        self.assertEqual(round(mac.macloren_arcsin(x, n), 3), answer)

    def test_mac_arccos(self):
        x = 1
        n = 2
        answer = 1.346
        self.assertEqual(round(mac.macloren_arccos(x, n), 3), answer)


if __name__ == '__main__':
    unittest.main()

