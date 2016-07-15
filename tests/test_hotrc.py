import os
from unittest import TestCase

from hotrc.hotrc import HotRC


class TestHotRC(TestCase):
    hotrc = None


    @classmethod
    def setUpClass(cls):
        cls.rcfile = '{}/.testrc'.format(os.path.dirname(__file__))
        open(cls.rcfile, 'w+').close()
        cls.hotrc = HotRC(bashrc=cls.rcfile)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.rcfile)

    def test_rcfile(self):
        self.assertTrue(os.path.isfile(self.hotrc.BASHRC))
