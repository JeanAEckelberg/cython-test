from setuptools import setup
from Cython.Build import cythonize

setup(
    name='adder',
    ext_modules=cythonize('adder.pyx'),
)