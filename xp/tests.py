import unittest
from django.test import TestCase

# Create your tests here.
from xp.views import level


class XpTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(level(0), 'Level1 Xp 0<br/>0..........100')
        self.assertEqual(level(210), 'Level2 Xp 210<br/>100***.......400')
        self.assertEqual(level(1210), 'Level4 Xp 1210<br/>900****......1600')
