from setuptools import setup
from japan_holiday import __version__
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='japan_holiday',
    version=__version__,
    description='Japanese TF-IDF',
    long_description=long_description,
    author='haminiku',
    author_email='haminiku1129@gmail.com',
    url='https://github.com/subc/japan_holiday',
    packages=['japan_holiday'],
    package_dir={'japan_holiday': 'japan_holiday'},
    include_package_data=True,
    install_requires=['requests >= 2.0'],
    license='MIT License',
    zip_safe=False,
    keywords=['holiday', 'japan_holiday'],
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
