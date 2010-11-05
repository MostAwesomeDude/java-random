#!/usr/bin/env python

import unittest

import javarandom

class AccuracyTest(unittest.TestCase):

    def setUp(self):
        self.r = javarandom.Random(0)

    def test_trivial(self):
        pass

    def test_nextInt(self):
        standard = -1155484576
        self.assertEqual(self.r.nextInt(), standard)

if __name__ == "__main__":
    unittest.main()
