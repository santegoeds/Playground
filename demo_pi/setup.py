#!/usr/bin/env python 

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

cython = Extension(
    "monte_carlo.cython",
    extra_compile_args= [
        "-fopenmp"
    ],
    extra_link_args = [
        "-fopenmp",
        "-lm",
    ],
    sources = [
        "src/cython.pyx"
    ],
)

setup(
    cmdclass = {
        "build_ext": build_ext
    },
    ext_modules = [
        cython,
    ]
)

