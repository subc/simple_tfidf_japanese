from setuptools import setup
from simple_tfidf_japanese import __version__
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='simple_tfidf_japanese',
    version=__version__,
    description='Japanese TF-IDF',
    long_description=long_description,
    author='haminiku',
    author_email='haminiku1129@gmail.com',
    url='https://github.com/subc/simple_tfidf_japanese',
    packages=['simple_tfidf_japanese'],
    package_dir={'simple_tfidf_japanese': 'simple_tfidf_japanese'},
    include_package_data=True,
    install_requires=['requests >= 2.0',
                      'nltk >= 3.1',
                      'janome >= 0.2.5',
                      'beautifulsoup4 >= 4.4.1'],
    license='MIT License',
    zip_safe=False,
    keywords=['tfidf', 'TF-IDF', 'Japanese'],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
