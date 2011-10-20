#!/usr/bin/env python 

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

cython_1 = Extension(
    "calculator.cython_1",
    #extra_compile_args=["-g"],
    #extra_link_args=["-g"],
    #language="c++",
    sources=["src/cython_1.pyx"],
)

cython_2 = Extension(
    "calculator.cython_2",
    #extra_compile_args=["-g"],
    extra_link_args=["-lm"],
    #language="c++",
    sources=["src/cython_2.pyx"],
)

setup(
    cmdclass = {
        'build_ext': build_ext
    },
    ext_modules = [
        cython_1,
        cython_2,
    ]
)

