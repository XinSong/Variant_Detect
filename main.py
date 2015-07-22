#!/usr/bin/env python
#coding=gbk
"""变体识别程序main模块
主要功能：1. 处理输入输出格式；2. 调用variant.py模块进行变体识别
"""

import sys
import logging
sys.path.append('lib')
sys.path.append('conf')
sys.path.append('dict')

import variant
import conf

def main(input):
    """变体识别程序main函数,入口程序
    Args:
        input: 待判定创意文件，每行为一条创意。格式:userid, planid, unitid, ideaid, title, description1, description2
    Return:
        None
    """
    logging.basicConfig(filename='log/variant_detect.log', level=logging.INFO)
    variant_detector = variant.VariantDetector(conf.YOUXI_BRAND_PATH)
    wordid = 0
    algorithmid = 83
    usertypeid = 0
    for line in input:
        vec = line.strip().split("\t")
        if len(vec) <= 5:
            logging.error("错误的创意记录: " + line)
            continue
        userid = vec[0]
        planid = vec[1]
        unitid = vec[2]
        ideaid = vec[3]
        idea = '\t'.join(vec[4:])
        variant_type, original_brand, variant_brand = variant_detector.detect(idea)
        if variant_type != 0 and variant_type != 1:
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % \
                (variant_type, original_brand, variant_brand, userid, \
                 planid, unitid, wordid, ideaid, algorithmid, usertypeid, idea)

if __name__ == "__main__":
    main(sys.stdin)
