#coding=gbk
"""
This module provide two functions:
    1. Get stroke string for chinese character strings,
    2. Get distance between two different chinese character strings.
Authors: IVoid Song(songxin02@baidu.com)
DATE:    2015-03-31
"""
__all__ = ['get', 'get_dist']

import os
import sys
import logging

#��ʼ�����ֱʻ��ֵ�stroke_code_book
stroke_code_book = dict()
code_book = os.path.join(os.path.dirname(__file__), "stroke.code_book")
try:
    with open(code_book, 'r') as f:
        for line in f:
            vec = line.strip().split('\t')
            if len(vec) != 2:
                logging.error("�ʻ�����ʽ�����ļ�:" + code_book + ",��¼:" + line)
                sys.exit(1)
            stroke_code_book[vec[1].decode('gbk')] = vec[0]
except IOError as e:
    logging.error("Can't found " + code_book)
    sys.exit(1)

def isChinese(s, encoding='gbk'):
    try:
        chars = s.decode(encoding)
    except UnicodeDecodeError as e:
        return False
    
    for char in chars:
        if char != ' ' and char not in stroke_code_book:
            return False
    return True

def get(s, delimiter="", encoding='gbk'):
    """���غ����ַ���s��Ӧ�ıʻ��ַ���.
    Args:
        s: �����ַ���
        delimiter: ���صıʻ��ַ�������ͬ����֮��ļ��
        encoding: �����ַ���s�ı��뷽ʽ
    Return:
        �ַ����������ַ���s��Ӧ�ıʻ��ַ���
    Attention: 
        ע�⣬���s�а�����Ϊ���ֵ��ַ�����ö�Ӧ�ַ��ıʻ��᷵�ؿ��ַ�����
    """
    return delimiter.join(_stroke_generator(s, encoding))


def get_dist(charsA, charsB):
    """�������������ַ���charsA��charsB֮��ʻ��ı༭���롣
    Args:
        charsA�������ַ���A
        charsB: �����ַ���B
    Return:
        λ��[0,1]֮��ĸ���������ʾcharsA��charsB֮��ʻ��ı༭���롣0��ʾ��ȫһ�£�1��ʾ��ȫ��ͬ��
    Attention:
        ע�⣬��charsA��charsB֮��ֻ��һ��ƫ�Բ��ף�����༭������롣
        
    """
    seqA = get(charsA)
    seqB = get(charsB)

    if seqA == "" or seqB == "":
        return float("inf")
    
    if len(seqA) < len(seqB):
        seqA, seqB = seqB, seqA

    head = 0
    while head < len(seqB) and seqA[head] == seqB[head]:
        head += 1

    if seqB[head:] in seqA[head:]:
        #���һ��Ψһ��ƫ�Բ���ʱcost����
        return (len(seqA) - len(seqB)) * 0.5 / len(seqB)
    else:
        return  _stroke_edit_dist(seqA, seqB) * 1.0 / len(seqB)


def _stroke_generator(chars, encoding):
    """���ɺ����ַ���chars�ıʻ�����.���chars�а����������ַ������Ӧ�ַ��ıʻ��ᱻ����Ϊ���ַ�����
    Args:
        chars: �ַ���
        encoding��chars�ı��뷽ʽ
    Return:
        �������������ַ���chars�ıʻ�
    """
    try:
        chars = chars.decode(encoding)
    except UnicodeDecodeError as e:
        logging.error("Incorrect encodings: " + chars + "  " + encoding)
        raise StopIteration

    for char in chars:
        if char in stroke_code_book:
            yield stroke_code_book[char]
        else:
            yield ""


def _stroke_edit_dist(seqA, seqB):
    """���ö�̬�滮������seqA��seqB�ı༭���롣
    Args:
        seqA: �ʻ�����A
        seqB���ʻ�����B
    Return��
        �������ʻ�����A�ͱʻ�����B�ı༭����
    """
    if seqA == "":
        return len(seqB)
    if seqB == "":
        return len(seqA)

    pre = range(0, len(seqA) + 1)
    post = [0] * (len(seqA) + 1)
    for i in range(1, len(seqB) + 1):
        post[0] = i
        for j in range(1, len(seqA) + 1):
            if seqB[i - 1] == seqA[j - 1]:
                post[j] = pre[j - 1]
            else:
                post[j] = min(post[j - 1] + 1, pre[j - 1] + 1, pre[j] + 1)
        pre = post[:]
    return post[len(seqA)]
