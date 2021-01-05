from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy


complie_flags = ['-std=c++11']
linker_flags = []


module = Extension(
    'target_encode_cy',
    ['target_encode_cy.pyx'],
    language = 'c++',
    include_dirs = [numpy.get_include()], #
    extra_compile_args = complie_flags,
    extra_link_args = linker_flags,
)


setup(
    name = 'zyt',
    ext_modules = cythonize(module),
    gdb_debug = False,
)