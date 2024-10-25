from setuptools import setup, Extension
import os

extension = Extension('cbbs', ['cbbs.c'])

setup(
    name="cbbs",
    version="1.0.0",
    author='wood',
    author_email='miraclerinwood@gmail.com',
    url='https://github.com/Rin-Wood/cbbs',
    description="bbs Decryption",
    long_description=open('README.md', 'rb').read().decode('utf8'),
	long_description_content_type='text/markdown',
    license="BSD",
    keywords="cbbs",
    ext_modules=[extension],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    python_requires=">=3.6",
)