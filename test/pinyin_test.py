#coding= gbk
"""Unit Test for pinyin.py
"""

import unittest
import pinyin

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get(self):
        """Test function pinyin.get 
        """
        self.assertEqual(pinyin.get('你好'), u'nihao')
        self.assertEqual(pinyin.get('你好吗?'), u'nihaoma?')
        self.assertEqual(pinyin.get('你好吗？'), u'nihaoma？')
        self.assertEqual(pinyin.get('你好'), u'nihao')
        self.assertEqual(pinyin.get('叶'), u'ye')
        
        self.assertEqual(pinyin.get('你好', " "), u'ni hao')
        self.assertEqual(pinyin.get('你好吗?', " "), u'ni hao ma ?')
        self.assertEqual(pinyin.get('你好吗？', " "), u'ni hao ma ？')

    def test_get_consonant(self):
        """Test function pinyin.get_consonant
        """
        self.assertEqual(pinyin.get_consonant('你好'), u'n h')
        self.assertEqual(pinyin.get_consonant('你好吗?'), u'n h m ?')
        self.assertEqual(pinyin.get_consonant('你好吗？'), u'n h m ？')
        self.assertEqual(pinyin.get_consonant('我爱你'), 'w  n')
        self.assertEqual(pinyin.get_consonant('爱'), u'')

        self.assertEqual(pinyin.get_consonant('你好'), u'n h')
        self.assertEqual(pinyin.get_consonant('你好', "-"), u'n-h')
        self.assertEqual(pinyin.get_consonant('你好吗?', "-"), u'n-h-m-?')
        self.assertEqual(pinyin.get_consonant('你好吗？', "-"), u'n-h-m-？')

    def test_get_vowel(self):
        """Test function pinyin.get_vowel
        """
        self.assertEqual(pinyin.get_vowel('你好'), u'i ao')
        self.assertEqual(pinyin.get_vowel('你好吗?'), u'i ao a ?')
        self.assertEqual(pinyin.get_vowel('你好吗？'), u'i ao a ？')
        self.assertEqual(pinyin.get_vowel('你好'), u'i ao')
        self.assertEqual(pinyin.get_vowel('我爱你'), u'o ai i')
        self.assertEqual(pinyin.get_vowel('爱'), u'ai')

        self.assertEqual(pinyin.get_vowel('你好', '-'), u'i-ao')
        self.assertEqual(pinyin.get_vowel('你好吗?', "-"), u'i-ao-a-?')

    def test_numbers(self):
        """Test the get/get_consonant/get_vowel function for arabic numbsers
        """
        self.assertEqual(pinyin.get('2'), u'er')
        self.assertEqual(pinyin.get('1234567890'), u'yiersansiwuliuqibajiuling')
        self.assertEqual(pinyin.get_consonant('1'), u'y')
        self.assertEqual(pinyin.get_vowel('1'), u'i')

    def test_mixed_chinese_english_input(self):
        """Test the get/get_consonant/get_vowel function for mixed chinese english string
        """
        self.assertEqual(pinyin.get('hi你好'), u'hinihao')
        self.assertEqual(pinyin.get_consonant('hi你好'), u'h i n h')
        self.assertEqual(pinyin.get_vowel('hi你好'), u'h i i ao')


if __name__ == '__main__':
    unittest.main()
