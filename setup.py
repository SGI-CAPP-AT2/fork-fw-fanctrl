from setuptools import setup, Extension
from Cython.Build import cythonize
import os

csrc_dir = os.path.abspath("./csrc")

shgi_mod = Extension(
    "lib_example.shgi_mod",  # Note the dotted name here!
    sources=["src/lib_example/src/wrapper.pyx", "src/lib_example/csrc/lib.c"],
    include_dirs=[csrc_dir],
)

setup(
    ext_modules=cythonize(shgi_mod),
    include_dirs=[csrc_dir],
    package_dir={'': 'src'}, # Tell setuptools where the packages are
    packages=['lib_example'], # Important: List the package(s)
)