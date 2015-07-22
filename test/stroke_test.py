# -*- coding: gbk -*-
"""Unit Test for stroke.py
"""

import unittest
import stroke

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get(self):
        """Test function stroke.get
        """
        self.assertEqual(stroke.get('我'), u'phshzpn')
        self.assertEqual(stroke.get('我爱百度'), u'phshzpnpnnpnzhpznhpszhhnhphsshzn')
        self.assertEqual(stroke.get('我爱MOOC'), u'phshzpnpnnpnzhpzn')
        self.assertEqual(stroke.get('我爱百度', "-"), u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn')
        self.assertEqual(stroke.get('我爱百度'.decode('gbk').encode('utf-8'), "-", 'utf-8'), 
                         u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn')
        self.assertEqual(stroke.get('我爱百度！', "-"), u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn-')

    def test_get_dist(self):
        """Test function stroke.get_dist
        """
        self.assertEqual(stroke.get_dist("微言", "微信"), 0.05)
        self.assertEqual(stroke.get_dist("微亻言", "微信"), 0)
        self.assertEqual(stroke.get_dist("微言", "微信"), stroke.get_dist("微信", "微言"))
        self.assertEqual(stroke.get_dist("秦", "泰"), 0.3)

if __name__ == '__main__':
    unittest.main()
