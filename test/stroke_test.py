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
        self.assertEqual(stroke.get('��'), u'phshzpn')
        self.assertEqual(stroke.get('�Ұ��ٶ�'), u'phshzpnpnnpnzhpznhpszhhnhphsshzn')
        self.assertEqual(stroke.get('�Ұ�MOOC'), u'phshzpnpnnpnzhpzn')
        self.assertEqual(stroke.get('�Ұ��ٶ�', "-"), u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn')
        self.assertEqual(stroke.get('�Ұ��ٶ�'.decode('gbk').encode('utf-8'), "-", 'utf-8'), 
                         u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn')
        self.assertEqual(stroke.get('�Ұ��ٶȣ�', "-"), u'phshzpn-pnnpnzhpzn-hpszhh-nhphsshzn-')

    def test_get_dist(self):
        """Test function stroke.get_dist
        """
        self.assertEqual(stroke.get_dist("΢��", "΢��"), 0.05)
        self.assertEqual(stroke.get_dist("΢����", "΢��"), 0)
        self.assertEqual(stroke.get_dist("΢��", "΢��"), stroke.get_dist("΢��", "΢��"))
        self.assertEqual(stroke.get_dist("��", "̩"), 0.3)

if __name__ == '__main__':
    unittest.main()
