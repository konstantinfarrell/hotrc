import os
import sys
from unittest import TestCase

from hotrc.hotrc import HotRC, start


class TestHotRC(TestCase):
    hotrc = None

    @classmethod
    def setUpClass(cls):
        ''' Create a test rc file and a hotrc object prove '''
        cls.rcfile = '{}/.testrc'.format(os.path.dirname(__file__))
        open(cls.rcfile, 'w+').close()
        cls.hotrc = HotRC(bashrc=cls.rcfile)

    @classmethod
    def tearDownClass(cls):
        ''' Remove the test rc file after tests '''
        os.remove(cls.rcfile)

    def test_rcfile(self):
        ''' Make sure the rc file was created '''
        self.assertTrue(os.path.isfile(self.hotrc.BASHRC))

    def test_read_bashrc(self):
        ''' Make sure the content is being read from the
        rc file correctly.
        '''
        content = 'foo'
        with open(self.hotrc.BASHRC, 'w+') as f:
            f.write(content)
        result = self.hotrc.read_bashrc()
        self.assertIn(content, result)
        with open(self.hotrc.BASHRC, 'w') as f:
            f.write('')

    def test_write_to_bashrc(self):
        ''' Tests that a key and value are
        correctly added to the rc file.
        '''
        key = 'foo'
        value = 'bar'
        self.hotrc.write_to_bashrc(key, value)
        result = self.hotrc.read_bashrc()
        self.assertIn(key, result)
        self.assertIn(value, result)

    def test_get_info(self):
        ''' Tests that the get_info() function is
        able to properly parse info from the rc file.
        '''
        test_info = '{}/test_info'.format(os.path.dirname(__file__))
        with open(test_info, 'w+') as f:
            f.write(self.hotrc.BASHRC)
        temp = self.hotrc.BASHRC
        self.hotrc.BASHRC = ''
        self.hotrc.get_info(test_info)
        self.assertEqual(self.hotrc.BASHRC, temp)
        os.remove(test_info)

    def test_get_aliases(self):
        ''' Tests to make sure the aliases are read
        from the rc file correctly.
        '''
        self.hotrc.write_to_bashrc('foo', 'bar')
        result = self.hotrc.get_aliases()
        self.assertIn(str(result), "{'foo': 'bar'}")
        test_info = '{}/test_info'.format(os.path.dirname(__file__))
        with open(test_info, 'w+') as f:
            f.write(self.hotrc.BASHRC)
        self.hotrc.BASHRC = ''
        result = self.hotrc.get_aliases(info_file=test_info)
        self.assertIn(str(result), "{'foo': 'bar'}")

    def test_create_alias(self):
        ''' Tests to make sure an alias is created correctly. '''
        key = 'foo'
        value = 'bar'
        self.hotrc.create_alias(key, value)
        result = self.hotrc.get_aliases()
        self.assertIn(key, result.keys())
        self.assertEqual(str(value), str(result.get(key, None)).replace('"',''))

    def test_remove_alias(self):
        ''' Tests to ensure an alias can be properly removed '''
        key = 'foo'
        value = 'bar'
        self.hotrc.write_to_bashrc(key, value)
        result = self.hotrc.get_aliases()
        self.assertIn(key, result.keys())
        self.hotrc.remove_alias(key)
        result = self.hotrc.get_aliases()
        self.assertNotIn(key, result.keys())

    def test_get_index_range_of_definitions(self):
        ''' Tests to make sure the index of the rc file where the HOTRC
        definitions begin exists.
        '''
        result = self.hotrc.get_index_range_of_definitions()
        self.assertNotEqual(result[0], -1)
        with open(self.hotrc.BASHRC, 'w') as f:
            f.write('')
        result = self.hotrc.get_index_range_of_definitions()
        self.assertEqual(result[0], 1)

    def test_start_new(self):
        ''' Tests start method to ensure new
        alias is added
        '''
        start(args=['add', 'foo', 'bar'], rcfile=self.hotrc.BASHRC)
        with open(self.hotrc.BASHRC, 'r') as result:
            result = result.read()
            self.assertIn('foo', result)
            self.assertIn('bar', result)

    def test_start_remove(self):
        ''' Tests start method to ensure alias is removed '''
        start(args=['add', 'foo', 'bar'], rcfile=self.hotrc.BASHRC)
        start(args=['rm', 'foo', 'bar'], rcfile=self.hotrc.BASHRC)
        with open(self.hotrc.BASHRC, 'r') as result:
            result = result.read()
            self.assertNotIn('foo', result)
            self.assertNotIn('bar', result)
        start(args=['add', 'foo', 'bar'], rcfile=self.hotrc.BASHRC)
        start(args=['rm', 'foo'], rcfile=self.hotrc.BASHRC)
        with open(self.hotrc.BASHRC, 'r') as result:
            result = result.read()
            self.assertNotIn('foo', result)
            self.assertNotIn('bar', result)
