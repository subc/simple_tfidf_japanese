# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from simple_tfidf_japanese import TFIDF


def test_similarity():
    # TFIDF.similarity Test
    tfidf1_sample = [['Apple', 1], ['Orange', 2], ['Banana', 1], ['Kiwi', 0]]
    tfidf2_sample = [['Apple', 1], ['Orange', 0], ['Banana', 2], ['Kiwi', 1]]

    # Tf-Idf cosは0.5であること
    r = TFIDF.similarity(tfidf1_sample, tfidf2_sample)
    assert round(r - 0.5, 7) == 0

    # 同じTf-IdfはTf-Idf cosが1.0であること
    r = TFIDF.similarity(tfidf1_sample, tfidf1_sample)
    assert round(r - 1, 7) == 0


def test_tfidf():
    # 中日
    url = "https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E3%83%A4%E3%82%AF%E3%83%AB%E3%83%88%E3%82%B9%E3%83%AF%E3%83%AD%E3%83%BC%E3%82%BA"
    tfidf1 = TFIDF.gen_web(url)

    # 山本昌
    url = "https://ja.wikipedia.org/wiki/%E5%B1%B1%E6%9C%AC%E6%98%8C"
    tfidf2 = TFIDF.gen_web(url)

    # print tfidf1
    for k, v in tfidf1:
        print k, v

    print "~~~~~~~~~~~~~~~"

    # print tfidf2
    for k, v in tfidf2:
        print k, v

    print TFIDF.similarity(tfidf1, tfidf2)


def test_tfidf_multi():
    # 山本昌
    _base_url = "https://ja.wikipedia.org/wiki/%E5%B1%B1%E6%9C%AC%E6%98%8C"

    # 比較対象
    data = [
        ['巨人',
         'https://ja.wikipedia.org/wiki/%E8%AA%AD%E5%A3%B2%E3%82%B8%E3%83%A3%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%84'],
        ['中日', 'https://ja.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E3%83%89%E3%83%A9%E3%82%B4%E3%83%B3%E3%82%BA'],
        ['サッカー日本代表',
         'https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%83%E3%82%AB%E3%83%BC%E6%97%A5%E6%9C%AC%E4%BB%A3%E8%A1%A8'],
    ]

    # 計算
    result = TFIDF.some_similarity(_base_url, data)

    # 結果表示
    result.sort(key=lambda x: x[2], reverse=True)
    for title, url, value in result:
        print title, value
