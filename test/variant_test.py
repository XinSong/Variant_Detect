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
        idea1 = "2014全新的捕鱼达人.各种捕鱼游戏 千人在线达人捕鱼    捕鱼达人网络版,9900炮打鱼,超刺激捕鱼游首选!"
        idea2 = "2015{梦幻剑侠},今日 一起浪迹天涯《天涯明月刀》  {梦幻剑侠},与全球天刀粉丝 一起浪迹天涯" 
        idea3 = "{好玩不花钱网游}《洛神》,2015内测新服火爆开启!  省钱!《洛神》,2.5D仙侠PK网游神作,装备1次打造终身受益"

        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea1), \
                         set(['捕鱼达人']))
        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea2), \
                         set(['梦幻剑侠', "天涯明月刀"]))
        self.assertEqual(self.variant._VariantDetector__get_valid_brand(idea3), \
                         set(['洛神']))
    
    def test_detect(self):
        """Test function variant.detect
        """
        idea1 = "2014全新的捕鱼达人.各种捕鱼游戏 千人在线达人捕鱼    捕鱼达人网络版,9900炮打鱼,超刺激捕鱼游首选!"
        idea2 = "2015{梦幻剑侠},今日 一起浪迹天涯《天涯明月刀》  {梦幻剑侠},与全球天刀粉丝 一起浪迹天涯" 
        idea3 = "{好玩不花钱网游}《洛神》,2015内测新服火爆开启!  省钱!《洛神》,2.5D仙侠PK网游神作,装备1次打造终身受益"
        idea4 = "2014全新武侠页游《神战传奇》酷炫3D武侠页游! 加入《神战传奇》让你扬名立万!号令群雄!称霸武林!"
        idea5 = "2014东方经典武侠《{剑OL仙}》极具武侠韵味页游    如梦似幻的武侠题材,华丽震撼的游戏画面"
        idea6 = "2014火爆游戏 {千炮捕渔下载} 做捕鱼牛人  {千炮捕渔下载},亿万玩家一致好评,流畅的画面,不一样的体验"
        
        self.assertEqual(self.variant.detect(idea1), (0, "", ""))
        self.assertEqual(self.variant.detect(idea2), (0, "", ""))
        self.assertEqual(self.variant.detect(idea3), (0, "", ""))
        self.assertEqual(self.variant.detect(idea4), (1, "战神传奇", "神战传奇"))
        self.assertEqual(self.variant.detect(idea5), (2, "剑仙", "剑仙"))
        self.assertEqual(self.variant.detect(idea6), (4, "千炮捕鱼", "千炮捕渔"))

    def test_is_reverse_brand(self):
        """Test private function variant.__is_reverse_brand
        """
        self.assertEqual(self.variant._VariantDetector__is_reverse_brand(["达人捕鱼"]), \
                         (1, "捕鱼达人", "达人捕鱼"))
        self.assertEqual(self.variant._VariantDetector__is_reverse_brand(["仙剑"]), (0, "", ""))

    def test_is_contain_alpha(self):
        """Test private function variant.__is_contain_alpha
        """
        self.assertEqual(self.variant._VariantDetector__is_contain_alpha("剑仙"), False)
        self.assertEqual(self.variant._VariantDetector__is_contain_alpha("剑OL仙"), True)

    def test_corresponding_discord(self):
        """Test private function variant.__corresponding_discord
        """
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("捕鱼达人", "捕鱼达人"), 0)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("捕鱼达人", "捕渔达人"), 1)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("捕鱼达人", "捕渔大人"), 2)
        self.assertEqual(self.variant._VariantDetector__corresponding_discord("捕鱼达人", "捕渔人"), \
                         float("inf"))

    def test_find_discord_pos(self):
        """Test private function variant.__find_discord_pos
        """
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("捕鱼达人", "捕渔达人"), 1)
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("捕鱼达人", "捕渔大人"), 1)
        self.assertEqual(self.variant._VariantDetector__find_discord_word_pos("捕鱼达人", "捕鱼达人"), -1)

    def test_get_clause_word_list(self):
        """Test private function variant.__get_clause_word_list
        """
        clause1 = "《剑OL仙》"
        self.assertEqual(self.variant._VariantDetector__get_clause_word_list(clause1), \
                         (["剑OL仙", "剑OL", "OL仙", "OL", "仙", "剑"], ["剑仙"]))
        clause2 = "首次充值立享《4折》优惠"
        words2 = ["立享4折优惠", "首次充值立享4", "充值立享4折", "充值立享4",\
                  "立享4折", "首次充值立享", "享4折优惠", "享4折", "首次充值立", "4折优惠", \
                  "立享4", "充值立享", "折优惠", "4折", "首次充值", "立享", "充值立", "享4", \
                  "享", "立", "折", "首次", "充值", "优惠", "4"]
        words_2_sep_gram = ["享折", "立4", "充值享", "4优惠"]
        self.assertEqual(self.variant._VariantDetector__get_clause_word_list(clause2), \
                         (words2, words_2_sep_gram))

    def test_pronounciation_detect(self):
        """Test private function variant.__pronounciation_detect
        """
        clause1 = "名将之三国ol盛世公测"
        words1, words_1_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause1)
        words1 += words_1_sep_gram
        clause2 = "酷wo音乐海量音乐免费听"
        words2, words_2_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause2)
        words2 += words_2_sep_gram
        clause3 = "免费下载苹果版<刀塔传骑>"
        words3, words_3_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause3)
        words3 += words_3_sep_gram
        clause4 = "今日訷途火爆新区发布"
        words4, words_4_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause4)
        words4 += words_4_sep_gram

        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words1, clause1), \
                         (2, "名将三国", "名将三国"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words2, clause2), \
                         (3, "酷我音乐", "酷wo音乐"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words3, clause3), \
                         (4, "刀塔传奇", "刀塔传骑"))
        self.assertEqual(self.variant._VariantDetector__pronounciation_detect(words4, clause4), \
                         (8, "神途", "訷途"))
    
    def test_stroke_seq_detect(self):
        """Test private function variant.__stroke_seq_detect
        """
        clause1 = "{Z逍遥官方充值}国游网超省钱的海外游戏点卡商城"
        words1, words_1_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause1)
        clause2 = "点击领礼包看英雄Z剑攻略!"
        words2, words_2_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause2)
        clause3 = "{太极熊喵首充号充值}:选7881!"
        words3, words_3_sep_gram = self.variant._VariantDetector__get_clause_word_list(clause3)
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words1), \
                         (6, "醉逍遥", "Z逍遥"))
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words2), \
                         (6, "英雄之剑", "英雄Z剑"))
        self.assertEqual(self.variant._VariantDetector__stroke_seq_detect(words3), \
                         (7, "太极熊猫", "太极熊喵"))

    def test_preprocess(self):
        """Test private function variant.__preprocess
        """
        idea1 = "{关键词}{太极熊喵首充号充值}:选7881! 创 建新太极熊账号,首次充值立享《4折》优惠,首充代充钻石持续4折起,安全有保障!"
        clean1 = "太极熊喵首充号充值\t:选7881\t创建新太极熊账号\t首次充值立享《4折》优惠\t首充代充钻石持续4折起\t安全有保障"
        self.assertEqual(self.variant._VariantDetector__preprocess(idea1), clean1)

if __name__ == "__main__":
    unittest.main()
