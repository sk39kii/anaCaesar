# -*- coding: utf-8 -*-

u"""シーザ暗号の解析サポート
Analysis support of Caesar cipher
Abridged edition
"""
__version__ = '0.0.1'
__date__ = '2016/03/28'
__status__ = 'development'
__author__ = 'sk39kii <sk39kii@gmail.com>'

import sys
import curses.ascii

def anaCaesar(encryptoStr, ic=True):
    u"""シーザー暗号の文字列を解析
    """
    types = 26
    if not ic:
        types = 26 * 2

    for i in range(1, types + 1):
        decStr = ''
        for c in list(encryptoStr):
            decStr += shift_AlphabetOnly(c, i, ic)

        print '{}\t{}'.format(i, decStr)


def shift_AlphabetOnly(character, size, ic=True):
    u"""文字のシフト
    character: 復号対象の文字(アルファベットのみ)
    size: ずらす大きさ
    ic: 大文字小文字の区別フラグ
        ic=True: 区別しない(デフォルト)
        例：対象文字が'z'、1文字ずらすと'a' 対象文字が'Z'、1文字ずらすと'A'
            AZaz -> BAba
            復号後の文字範囲は、abc...xyz(復号前が大文字なら大文字、小文字なら小文字)
        ic=False: 区別する
        例：対象文字が'z'、1文字ずらすと'A' 対象文字が'Z'、1文字ずらすと'a'
            AZaz -> BabA
            復号後の文字範囲は、ABC...XYZabc...xyz
    """
    if not ic:
        A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        a = 'abcdefghijklmnopqrstuvwxyz'
        Aalist = list(A+a)
        index = Aalist.index(character) + size
        if index >= len(Aalist):
            return Aalist[index - len(Aalist)]
        else:
            return Aalist[index]
    else:
        maxchar = 'z'
        if character.isupper():
            maxchar = 'Z'
        if ord(character) + size > ord(maxchar):
            return chr(ord(character) + size - 26)
        else:
            return chr(ord(character) + size)


def anaCaesarAscii(encryptoStr):
    u"""シーザー暗号の文字列を解析
    文字の種類数 スペース(32:0x20) <= 対象文字 <= }(125:0x7d)
    """
    minCharCode = 32
    maxCharCode = 125
    # 文字の種類数(スペース(32:0x20) <= 対象文字 <= }(125:0x7d))
    types = maxCharCode - minCharCode + 1

    for i in range(1, types + 1):
        decStr = ''
        for c in list(encryptoStr):
            decStr += shift_ascii(c, i, minCharCode, maxCharCode, types)

        print '{}\t{}'.format(i, decStr)


def shift_ascii(character, size, minCharCode, maxCharCode, types):
    u"""文字のシフト
    character: 復号対象の文字(記号も含む)
        スペース(32:0x20) <= 対象文字 <= }(125:0x7d)
    size: ずらす大きさ
    """
    if minCharCode <= ord(character) <= maxCharCode:
        if ord(character) + size > maxCharCode:
            return chr(ord(character) + size - types)
        else:
            return chr(ord(character) + size)
    else:
        return ''


def print_ascii(border=False):
    u"""アスキーコードを出力
    border: 出力時にボーダー線を表示する
        ※デフォルト=False:表示しない
    """
    # minCharCode = 32
    # maxCharCode = 125
    minCharCode = 0
    maxCharCode = 127
    space = ' '*8
    for n in range(minCharCode, maxCharCode + 1):
        c = chr(n)
        # h = hex(n)
        h = '0x%02x' % (n)
        # h = '0x%02X' % (n)
        # ac = curses.ascii.ascii(c)
        uc = curses.ascii.unctrl(c)

        sep1 = ' '*(len(space) - len(str(n)))
        sep2 = ' '*(len(space) - len(h))
        if border:
            s = sep1
            sep1 = s[:len(s) - 3] + '|' + s[len(s) - 3:]
            s = sep2
            sep2 = s[:len(s) - 2] + '|' + s[len(s) - 2:]
            sep3 = ' '*(len(' '*4) - len(uc)) + '|'
            print '-'*26
            print '|  {}{}{}{}{}{}'.format(n, sep1, h, sep2, uc, sep3)
        else:
            print '{}{}{}{}{}'.format(n, sep1, h, sep2, uc)

    if border:
        print '-'*26

if __name__ == "__main__":
    if len(sys.argv) > 1:
        anaCaesar(sys.argv[1])

    # s = 'AZaz'
    # s = 'VwdbKxqjub'

    # 復号化 アルファベット のみ
    # anaCaesar(s)

    # アスキーコードを表示
    # print_ascii()

    # スペース(32:0x20)から }(125:0x7d)で復号化
    # anaCaesarAscii(s)
