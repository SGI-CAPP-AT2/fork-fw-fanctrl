from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

lib_example_ext = Extension(
    "lib_example.shgi_mod",
    sources=["src/lib_example/csrc/ectool_func.c", "src/lib_example/src/wrapper.pyx"],
    include_dirs=["src/lib_example/csrc"],
)

setup(
    name="fw_fanctrl",
    version="0.1.0",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},
    ext_modules=cythonize([lib_example_ext]),
)