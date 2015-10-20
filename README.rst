TF-IDF calculator system of Japanese language
====================================================

Python 日本語のTF-IDF計算機

日本語ドキュメント:  `White Paper`_

Features
--------
- TF-IDF from Web

Installation
-----------------

.. code-block:: bash

    $ pip install simple_tfidf_japanese

Sample Code
-----------------

.. code-block:: python

    # 文章からtfidfを出力(Get TF-IDF from text)
    from simple_tfidf_japanese import TFIDF
    text = "肉フェスNIIGATAで肉三昧の夜ごはん❤︎ステーキハウスあづまさんの雪室熟成新潟県産牛ステーキおいしい*\(^o^)/*お塩でもワサビでもぴったり！"
    tfidf1 = TFIDF.gen(text, enable_one_char=1)
    for key, value in tfidf1:
         print key, value

    >>> 肉 0.0952380952381
    >>> ステーキ 0.0952380952381
    >>> お 0.047619047619
    >>> ごはん 0.047619047619
    >>> 雪 0.047619047619
    >>> 新潟 0.047619047619
    >>> 熟成 0.047619047619
    ...

    # Webからtfidfを出力(Get TF-IDF from Web)
    url = "https://ja.wikipedia.org/wiki/%E6%B7%A1%E8%B7%AF%E3%83%93%E3%83%BC%E3%83%95"
    tfidf2 = TFIDF.gen_web(url)
    for key, value in tfidf2:
         print key, value

    >>> 淡路 0.0453257790368
    >>> ビーフ 0.0396600566572
    >>> 但馬 0.0198300283286
    >>> 淡路島 0.0169971671388
    >>> ページ 0.0169971671388
    >>> 表示 0.014164305949

    # TF-IDF Cosine Similarityで類似度を計算(calc TF-IDF Cosine Similarity)
    tfidf1 = [['Apple', 1], ['Orange', 2], ['Banana', 1], ['Kiwi', 0]]
    tfidf2 = [['Apple', 1], ['Orange', 0], ['Banana', 2], ['Kiwi', 1]]
    print TFIDF.similarity(tfidf1, tfidf2)
    >>> 0.5
    ...


.. _`White Paper`: http://qiita.com/haminiku/items/3c8f0d43d82c0d58d7da
