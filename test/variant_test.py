#coding=gbk
"""Test Case for variant.py
"""

import unittest
import variant

class VariantTest(unittest.TestCase):
    """Test Case for variant
    """
    
    @classmethod
    def setUpClass(cls):
        VariantTest.variant = variant.VariantDetector("brand.test")
    
    @classmethod
    def tearDownClass(cls):
        pass 
    
    def test_get_valid_brand(self):
        """Test function variant.get_valid_brand
        """
        idea1 = "2014ȫ�µĲ������.���ֲ�����Ϸ ǧ�����ߴ��˲���    ������������,9900�ڴ���,���̼���������ѡ!"
        idea2 = "2015{�λý���},���� һ���˼����ġ��������µ���  {�λý���},��ȫ���쵶��˿ һ���˼�����" 
        idea3 = "{���治��Ǯ����}������,2015�ڲ��·��𱬿���!  ʡǮ!������,2.5D����PK��������,װ��1�δ�����������"

        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea1), \
                         set(['�������']))
        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea2), \
                         set(['�λý���', "�������µ�"]))
        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea3), \
                         set(['����']))
    
    def test_detect(self):
        """Test function variant.detect
        """
        idea1 = "2014ȫ�µĲ������.���ֲ�����Ϸ ǧ�����ߴ��˲���    ������������,9900�ڴ���,���̼���������ѡ!"
        idea2 = "2015{�λý���},���� һ���˼����ġ��������µ���  {�λý���},��ȫ���쵶��˿ һ���˼�����" 
        idea3 = "{���治��Ǯ����}������,2015�ڲ��·��𱬿���!  ʡǮ!������,2.5D����PK��������,װ��1�δ�����������"
        idea4 = "2014ȫ������ҳ�Ρ���ս���桷����3D����ҳ��! ���롶��ս���桷������������!����Ⱥ��!�ư�����!"
        idea5 = "2014��������������{��OL��}������������ζҳ��    �����ƻõ��������,�����𺳵���Ϸ����"
        idea6 = "2014����Ϸ {ǧ�ڲ�������} ������ţ��  {ǧ�ڲ�������},�������һ�º���,�����Ļ���,��һ��������"
        
        self.assertEqual(self.variant.detect(idea1), (0, "", ""))
        self.assertEqual(self.variant.detect(idea2), (0, "", ""))
        self.assertEqual(self.variant.detect(idea3), (0, "", ""))
        self.assertEqual(self.variant.detect(idea4), (1, "ս����", "��ս����"))
        self.assertEqual(self.variant.detect(idea5), (2, "����", "����"))
        self.assertEqual(self.variant.detect(idea6), (4, "ǧ�ڲ���", "ǧ�ڲ���"))

    def test_is_reverse_brand(self):
        """Test private function variant.__is_reverse_brand
        """
        self.assertEqual(self.variant._VariantDetector__is_reverse_brand(["���˲���"]), \
                         (1, "�������", "���˲���"))
        self.assertEqual(self.variant._VariantDetector__is_reverse_brand(["�ɽ�"]), (0, "", ""))

    def test_is_contain_alpha(self):
        """Test private function variant.__is_contain_alpha
        """
        self.assertEqual(self.variant._VariantDetector__is_contain_alpha("����"), False)
        self.assertEqual(self.variant._VariantDetector__is_contain_alpha("��OL��"), True)

    def test_corresponding_discord(self):
        """Test private function variant.__corresponding_discord
        """
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("�������", "�������"), 0)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("�������", "�������"), 1)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("�������", "�������"), 2)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("�������", "������"), \
                         float("inf"))

    def test_find_discord_pos(self):
        """Test private function variant.__find_discord_pos
        """
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("�������", "�������"), 1)
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("�������", "�������"), 1)
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("�������", "�������"), -1)

    def test_get_clause_word_list(self):
        """Test private function variant.__get_clause_word_list
        """
        clause1 = "����OL�ɡ�"
        self.assertEqual(self.variant._VariantDetector__get_clause_word_list(clause1), \
                         (["��OL��", "��OL", "OL��", "OL", "��", "��"], ["����"]))
        clause2 = "�״γ�ֵ����4�ۡ��Ż�"
        words2 = ["����4���Ż�", "�״γ�ֵ����4", "��ֵ����4��", "��ֵ����4",\
                  "����4��", "�״γ�ֵ����", "��4���Ż�", "��4��", "�״γ�ֵ��", "4���Ż�", \
                  "����4", "��ֵ����", "���Ż�", "4��", "�״γ�ֵ", "����", "��ֵ��", "��4", \
                  "��", "��", "��", "�״�", "��ֵ", "�Ż�", "4"]
        words_2_sep_gram = ["����", "��4", "��ֵ��", "4�Ż�"]
        self.assertEqual(self.variant._VariantDetector__get_clause_word_list(clause2), \
                         (words2, words_2_sep_gram))

    def test_pronounciation_detect(self):
        """Test private function variant.__pronounciation_detect
        """
        clause1 = "����֮����olʢ������"
        words1, words_1_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause1)
        words1 += words_1_sep_gram
        clause2 = "��wo���ֺ������������"
        words2, words_2_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause2)
        words2 += words_2_sep_gram
        clause3 = "�������ƻ����<��������>"
        words3, words_3_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause3)
        words3 += words_3_sep_gram
        clause4 = "�����Y;����������"
        words4, words_4_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause4)
        words4 += words_4_sep_gram

        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words1, clause1), \
                         (2, "��������", "��������"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words2, clause2), \
                         (3, "��������", "��wo����"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words3, clause3), \
                         (4, "��������", "��������"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words4, clause4), \
                         (8, "��;", "�Y;"))
    
    def test_stroke_seq_detect(self):
        """Test private function variant.__stroke_seq_detect
        """
        clause1 = "{Z��ң�ٷ���ֵ}��������ʡǮ�ĺ�����Ϸ�㿨�̳�"
        words1, words_1_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause1)
        clause2 = "����������Ӣ��Z������!"
        words2, words_2_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause2)
        clause3 = "{̫�������׳�ų�ֵ}:ѡ7881!"
        words3, words_3_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause3)
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words1), \
                         (6, "����ң", "Z��ң"))
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words2), \
                         (6, "Ӣ��֮��", "Ӣ��Z��"))
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words3), \
                         (7, "̫����è", "̫������"))

    def test_preprocess(self):
        """Test private function variant.__preprocess
        """
        idea1 = "{�ؼ���}{̫�������׳�ų�ֵ}:ѡ7881! �� ����̫�����˺�,�״γ�ֵ����4�ۡ��Ż�,�׳������ʯ����4����,��ȫ�б���!"
        clean1 = "̫�������׳�ų�ֵ\t:ѡ7881\t������̫�����˺�\t�״γ�ֵ����4�ۡ��Ż�\t�׳������ʯ����4����\t��ȫ�б���"
        self.assertEqual(self.variant._VariantDetector__preprocess(idea1), clean1)

if __name__ == "__main__":
    unittest.main()
