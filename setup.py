import os

from distutils.core import setup, Extension
try:
    from Cython.Build import cythonize
except ImportError:
    import warnings
    cython_installed = False
    warnings.warn('Cython not installed, using pre-generated C source file.')
else:
    cython_installed = True


if cython_installed:
    python_source = 'vedis.pyx'
else:
    python_source = 'vedis.c'
    cythonize = lambda obj: [obj]
library_source = 'src/vedis.c'

vedis_extension = Extension(
    'vedis',
    sources=[python_source, library_source])

setup(
    name='vedis',
    version='0.3.1',
    description='Fast Python bindings for the Vedis embedded NoSQL database.',
    author='Charles Leifer',
    author_email='',
    ext_modules=cythonize(vedis_extension),
)
