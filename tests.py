#!/usr/bin/env python

import unittest

import javarandom

class AccuracyTest(unittest.TestCase):

    def setUp(self):
        self.r = javarandom.Random(0)

    def test_trivial(self):
        pass

    def test_nextBytes(self):
        standard = [96, -76, 32, -69, 56, 81, -39, -44]
        l = [None] * len(standard)
        self.r.nextBytes(l)
        self.assertEqual(l, standard)

    def test_nextInt(self):
        standard = -1155484576
        self.assertEqual(self.r.nextInt(), standard)

    def test_nextInt_lue(self):
        standard = 12
        self.assertEqual(self.r.nextInt(42), standard)

    def test_nextLong(self):
        standard = -4962768465676381896
        self.assertEqual(self.r.nextLong(), standard)

    def test_nextBoolean(self):
        standard = True
        self.assertEqual(self.r.nextBoolean(), standard)

    def test_nextFloat(self):
        standard = 0.730968
        self.assertEqual(self.r.nextFloat(), standard)

    def test_nextDouble(self):
        standard = 0.730968
        self.assertEqual(self.r.nextDouble(), standard)

    def test_nextGaussian(self):
        standard = 0.802533, -0.901546
        self.assertEqual((self.r.nextGaussian(), self.r.nextGaussian()),
            standard)

if __name__ == "__main__":
    unittest.main()
