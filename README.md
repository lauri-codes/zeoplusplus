# zeoplusplus
Python wrapper for the Zeo++ library.

## Installation
pip install .

## Getting the C++ part ready for packaging

By default the package comes with pre-build Voro++ shared library and prebuilt
Cython binding code. If you however need to re-create them, the following
instructions will help

### Voro++
Voro++ currently requires a separate build step, which has to be performed
before attempting the Cython build. This is done by adding the -fPIC flag to
the file in src/voro++/config.mk, and then creating a library file with

```sh
cd src/voro++/src
make
```
This will create the voro++ shared library file in src/voro++/src, which is
then linked in the Cython build by adding

```sh
libdirs = ["src/voro++/src"]
libraries = ['voro++']
```

to the extension definitions.

### Cython
The cython wrapper definitions live inside src/zeoplusplus. These bindings can
be recreated by first setting `USE_CYTHON=True` in setup.py, and then
recreating the bindings with:

```sh
python setup.py build_ext --inplace
```

Remember to disable cython in setup.py afterwards by setting `USE_CYTHON=False`
in setup.py.
