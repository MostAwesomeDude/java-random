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

    def test_nextLong(self):
        standard = -4962768465676381896
        self.assertEqual(self.r.nextLong(), standard)

if __name__ == "__main__":
    unittest.main()
