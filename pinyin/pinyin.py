#coding=gbk
"""
Inherit from Open Source Project https://github.com/lxyu/pinyin
Some Changes:
1. Add mult-encodings support, remove .compat.py(we don't need that);
2. Add pronounciations for arabic numbers;
3. For some characters which have multi-pronounciation, change the order of multi-pronounciation
4. Add two functions: get_consonant and get_vowel

Author: IVoid Song(songxin02@baidu.com)
Date:   2015-03-31
"""

__all__ = ['get', 'get_consonant', 'get_vowel']

import os
import sys
import logging

# init pinyin dict
pinyin_dict = {}
mandarin_dat = os.path.join(os.path.dirname(__file__), "Mandarin.dat")
try:
    with open(mandarin_dat) as f:
        for line in f:
            k, v = line.strip().split('\t')
            pinyin_dict[k] = v.lower().split(" ")[0][:-1]
except IOError as e:
    logging.error("Can't found" + mandarin_dat)
    sys.exit(1)

pinyin_char = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                   'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z'])
pinyin_consonant = set(['b', 'p', 'm', 'f', 'd', 't', 
                        'n', 'l', 'g', 'k', 'h', 'j',
                        'q', 'x', 'r', 'z', 'c', 's',
                        'y', 'w'])


def get(s, delimiter='', encoding='gbk'):
    """Return the pinyin string of the chinese characters string
    Args:
        s: the chinese character string  
        delimiter: the delimiter used in the returned pinyin string
        encoding: the encoding mode of s
    Return:
        the pinyin string of s
    Attention: if the string contains irregular character which is not chinese, 
               the irregular character itself will be returned           
    """
    return delimiter.join(_pinyin_generator(s, encoding))


def get_consonant(s, delimiter=' ', encoding='gbk'):
    """Return the consonant string of the chinese characters string
    Args:
        s: the chinese character string  
        delimiter: the dilimiter used in the returned consonant string
        encoding: the encoding mode of s
    Return:
        the consonant string of s
    Attention: if the string contains irregular character which is not chinese, 
               the irregular character itself will be returned           
     """
    return delimiter.join(_consonant_generator(s, encoding))


def get_vowel(s, delimiter=' ', encoding='gbk'):
    """Return the vowel string of the chinese characters string
    Args:
        s: the chinese character string  
        delimiter: the dilimiter used in the returned vowel string
        encoding: the encoding mode of s
    Return:
        the vowel string of s
    Attention: if the string contains irregular character which is not chinese, 
               the irregular character itself will be returned           
     """
    return delimiter.join(_vowel_generator(s, encoding))


def _pinyin_generator(chars, encoding):
    """Generate pinyin for chars, if char is not chinese character,
    itself will be returned.
    Args:
        chars: the chinese character string  
        encoding: the encoding mode of s
    Return:
        An iterator which can generate pinyin string of chars
    """
    try:
        chars = chars.decode(encoding)
    except UnicodeDecodeError as e:
        logging.error("Incorrect encodings:" + chars + "  " + encoding)
        raise StopIteration

    for char in chars:
        key = "%.4X" % ord(char)
        yield pinyin_dict.get(key, char)

def _consonant_generator(chars, encoding):
    """Generate consonant for chars, if char is not chinese character,
        itself will be returned.
    Args:
        chars: the chinese character string  
        encoding: the encoding mode of s
    Return:
        An iterator which can generate pinyin string of chars
    """
    try:
        chars = chars.decode(encoding)
    except UnicodeDecodeError as e:
        logging.error("Incorrect encodings: " + chars + "  " + encoding)
        raise StopIteration

    for char in chars:
        key = "%.4X" % ord(char)
        if key in pinyin_dict:
            if pinyin_dict[key][0] in pinyin_consonant:
                yield pinyin_dict[key][0]
            else:
                yield ""
        else:
            yield char


def _vowel_generator(chars, encoding):
    """Generate vowel for chars, if char is not chinese character,
        itself will be returned.
    Args:
        chars: the chinese character string  
        encoding: the encoding mode of s
    Return:
        An iterator which can generate vowel string of chars
    """
    try:
        chars = chars.decode(encoding)
    except UnicodeDecodeError as e:
        logging.error("Incorrect encodings: " + chars + "  " + encoding)
        raise StopIteration

    for char in chars:
        key = "%.4X" % ord(char)
        if key in pinyin_dict:
            if pinyin_dict[key][0] not in pinyin_consonant:
                yield pinyin_dict[key]
            elif pinyin_dict[key][1] != 'h':
                yield pinyin_dict[key][1:]
            else:
                yield pinyin_dict[key][2:]
        else:
            yield char

